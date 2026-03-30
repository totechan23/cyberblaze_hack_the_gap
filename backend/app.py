from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

complaints = []

@app.route("/")
def home():
    return {"message": "Backend running 🔥"}

@app.route("/auth/login", methods=["POST"])
def login():
    return jsonify({
        "message": "Login success",
        "role": "citizen"
    })

@app.route("/ai/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    if "danger" in message.lower() or "help" in message.lower():
        return jsonify({
            "reply": "🚨 SOS triggered!"
        })

    complaint = {
        "id": len(complaints) + 1,
        "text": message,
        "status": "Pending"
    }

    complaints.append(complaint)

    return jsonify({
        "reply": "✅ Complaint registered!"
    })

@app.route("/employee/dashboard")
def dashboard():
    return jsonify({
        "complaints": complaints
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)