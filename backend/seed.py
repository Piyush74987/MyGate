from utils.firestore_client import db
from models import user_model, household_model, visitor_model
from datetime import datetime

def seed_data():
    household = household_model("A-101", [])
    household_ref = db.collection("households").add(household)

    resident = user_model("Resident One", "res1@example.com", household_ref[1].id, "resident")
    guard = user_model("Guard One", "guard1@example.com", None, "guard")
    admin = user_model("Admin One", "admin1@example.com", None, "admin")

    db.collection("users").add(resident)
    db.collection("users").add(guard)
    db.collection("users").add(admin)

    visitor = visitor_model("Ramesh", "9999999999", "Delivery", household_ref[1].id)
    db.collection("visitors").add(visitor)

    print("✅ Seed data created successfully!")

if __name__ == "__main__":
    seed_data()
