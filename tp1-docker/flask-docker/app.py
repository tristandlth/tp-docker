import os
from flask import Flask
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/db")
def check_db():
    try:
        client.admin.command("ping")
        return "Connexion MongoDB OK"
    except PyMongoError as e:
        return f"Connexion MongoDB KO : {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)