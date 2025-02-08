from flask import Flask, render_template, request
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

app = Flask(__name__)

gauth = GoogleAuth()

#gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    gfile = drive.CreateFile({'title': file.filename})
    gfile.SetContentString(file.read().decode("latin-1"))  # Adjust encoding if needed
    gfile.Upload()

    return "File uploaded successfully to Google Drive!"


if __name__ == "__main__":
    #app.run(debug=False)
      app.run( debug=True)


