# backend/utils/firestore_client.py
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Absolute or relative path to your service account
SERVICE_ACCOUNT_PATH = os.path.join(os.path.dirname(__file__), "..", "serviceAccountKey.json")

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
