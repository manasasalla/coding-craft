from flask import Flask, render_template, request
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import json

app = Flask(__name__)

gauth = GoogleAuth()

gauth.LoadClientConfigFile("C:\\Users\\Saiteja\\Downloads\\client_secrets.json")  # Load credentials from JSON
SCOPES = ['https://www.googleapis.com/auth/drive.file']

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
    gfile.SetContentString(file.read().decode("latin-1"))  
    gfile.Upload()

    return "File uploaded successfully to Google Drive!"

if __name__ == "__main__":
    app.run(debug=True)
 








