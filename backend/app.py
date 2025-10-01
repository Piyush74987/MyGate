# backend/app.py

from flask import Flask, request, jsonify
from services import visitor_service, ai_service
from utils.firestore_client import db  # Firebase initialized here
from firebase_admin import messaging

app = Flask(__name__)

# =========================
# Helper function to send FCM push notifications
# =========================
def send_push_notification(token, title, body):
    if not token:
        return {"success": False, "error": "No FCM token provided"}

    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            token=token
        )
        response = messaging.send(message)
        return {"success": True, "response": response}
    except Exception as e:
        return {"success": False, "error": str(e)}

# =========================
# Root / health check
# =========================
@app.route("/", methods=["GET"])
def home():
    return {"status": "ok", "message": "MyGate backend is running"}

# =========================
# Visitor API routes
# =========================
@app.route("/approveVisitor", methods=["POST"])
def approve_visitor():
    try:
        print("Headers:", request.headers)
        print("Raw data:", request.data)
        data = request.json
        print("Parsed JSON:", data)
        
        result = visitor_service.approve_visitor(data["visitorId"], data["userId"])
        
        if result.get("success"):
            token = data.get("token")
            send_push_notification(token, "Visitor Approved", f"Visitor {data['visitorId']} has been approved")
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/denyVisitor", methods=["POST"])
def deny_visitor():
    try:
        data = request.json
        result = visitor_service.deny_visitor(data["visitorId"], data["userId"], data.get("reason", ""))
        
        if result.get("success"):
            token = data.get("token")
            send_push_notification(token, "Visitor Denied", f"Visitor {data['visitorId']} has been denied")
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/checkin", methods=["POST"])
def checkin():
    try:
        data = request.json
        result = visitor_service.checkin_visitor(data["visitorId"], data["userId"])
        
        if result.get("success"):
            token = data.get("token")
            send_push_notification(token, "Visitor Checked In", f"Visitor {data['visitorId']} has checked in")
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/checkout", methods=["POST"])
def checkout():
    try:
        data = request.json
        result = visitor_service.checkout_visitor(data["visitorId"], data["userId"])
        
        if result.get("success"):
            token = data.get("token")
            send_push_notification(token, "Visitor Checked Out", f"Visitor {data['visitorId']} has checked out")
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# =========================
# AI Copilot Chat route
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        return jsonify(ai_service.process_chat(data["prompt"]))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# =========================
# Run Flask App
# =========================
if __name__ == "__main__":
    app.run(port=5001, debug=True)
