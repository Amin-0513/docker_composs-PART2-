from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(
    os.getenv("MONGO_URI", "mongodb://mongodb:27017/"),
    serverSelectionTimeoutMS=2000
)

@app.route("/")
def home():
    return """
    <h1>Hello, World!</h1>
    <p>Docker Compose application is running.</p>
    """

@app.route("/newone")
def newFearyre():
    return """
    <html>
        <head>
            <title>Updated Docker Web App</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>Hello, World!</h1>
            <h2>New Feature Added Successfully!</h2>
            <p>This web application has been updated using Docker Compose.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    client.admin.command("ping")
    return {"web": "healthy", "database": "connected"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)