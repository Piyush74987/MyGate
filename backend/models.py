from datetime import datetime

# Firestore collections: users, households, visitors, events

def user_model(displayName, email, householdId, roles):
    return {
        "displayName": displayName,
        "email": email,
        "householdId": householdId,
        "roles": roles,
        "createdAt": datetime.utcnow()
    }

def household_model(flatNo, members):
    return {
        "flatNo": flatNo,
        "members": members
    }

def visitor_model(name, phone, purpose, hostHouseholdId):
    return {
        "name": name,
        "phone": phone,
        "purpose": purpose,
        "hostHouseholdId": hostHouseholdId,
        "status": "pending",  # pending | approved | denied | checked_in | checked_out
        "approvedBy": None,
        "approvedAt": None,
        "createdAt": datetime.utcnow()
    }

def event_model(event_type, actorUserId, subjectId, payload):
    return {
        "type": event_type,
        "actorUserId": actorUserId,
        "subjectId": subjectId,
        "payload": payload,
        "ts": datetime.utcnow()
    }
