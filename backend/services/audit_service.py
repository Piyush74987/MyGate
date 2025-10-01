from utils.firestore_client import db
from models import event_model

def log_event(event_type, actorUserId, subjectId, payload):
    db.collection("events").add(event_model(event_type, actorUserId, subjectId, payload))
