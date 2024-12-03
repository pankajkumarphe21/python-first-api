from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Vercel Deployed API!"})

@app.route("/user/<userId>")
def getUser(userId):
    return jsonify(f"Hi {userId}")

if __name__ == "__main__":
    app.run()
