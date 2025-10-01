from utils.firestore_client import db
from models import visitor_model, event_model
from datetime import datetime

def create_visitor(name, phone, purpose, householdId, userId):
    visitor = visitor_model(name, phone, purpose, householdId)
    ref = db.collection("visitors").add(visitor)
    db.collection("events").add(event_model("create", userId, ref[1].id, visitor))
    return {"id": ref[1].id, **visitor}

def approve_visitor(visitorId, userId):
    ref = db.collection("visitors").document(visitorId)
    visitor = ref.get().to_dict()
    if visitor["status"] != "pending":
        return {"error": "Invalid state"}
    ref.update({"status": "approved", "approvedBy": userId, "approvedAt": datetime.utcnow()})
    db.collection("events").add(event_model("approval", userId, visitorId, {"status": "approved"}))
    return {"success": True}

def deny_visitor(visitorId, userId, reason=""):
    ref = db.collection("visitors").document(visitorId)
    visitor = ref.get().to_dict()
    if visitor["status"] != "pending":
        return {"error": "Invalid state"}
    ref.update({"status": "denied", "approvedBy": userId, "approvedAt": datetime.utcnow()})
    db.collection("events").add(event_model("denial", userId, visitorId, {"reason": reason}))
    return {"success": True}

def checkin_visitor(visitorId, userId):
    ref = db.collection("visitors").document(visitorId)
    visitor = ref.get().to_dict()
    if visitor["status"] != "approved":
        return {"error": "Invalid state"}
    ref.update({"status": "checked_in"})
    db.collection("events").add(event_model("checkin", userId, visitorId, {}))
    return {"success": True}

def checkout_visitor(visitorId, userId):
    ref = db.collection("visitors").document(visitorId)
    visitor = ref.get().to_dict()
    if visitor["status"] != "checked_in":
        return {"error": "Invalid state"}
    ref.update({"status": "checked_out"})
    db.collection("events").add(event_model("checkout", userId, visitorId, {}))
    return {"success": True}
