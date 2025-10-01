#!/bin/bash

# ===== Backend Structure =====
mkdir -p backend/services
mkdir -p backend/utils

touch backend/app.py
touch backend/seed.py
touch backend/models.py
touch backend/requirements.txt
touch backend/.env
touch backend/serviceAccountKey.json

# Backend services
touch backend/services/auth_service.py
touch backend/services/visitor_service.py
touch backend/services/notify_service.py
touch backend/services/ai_service.py
touch backend/services/audit_service.py

# Backend utils
touch backend/utils/firestore_client.py
touch backend/utils/fcm_client.py
touch backend/utils/openai_client.py

# ===== Frontend Structure =====
mkdir -p frontend/templates
mkdir -p frontend/static/css
mkdir -p frontend/static/js
mkdir -p frontend/static/img

touch frontend/app.py
touch frontend/requirements.txt
touch frontend/.env

# Frontend templates (Jinja2 HTML)
touch frontend/templates/base.html
touch frontend/templates/login.html
touch frontend/templates/dashboard.html
touch frontend/templates/guard.html
touch frontend/templates/admin.html
touch frontend/templates/visitors.html
touch frontend/templates/chat.html

# Frontend static files
touch frontend/static/css/style.css
touch frontend/static/js/main.js
touch frontend/static/js/chat.js

# ===== Root Files =====
touch firestore.rules
touch postman_collection.json
touch run.sh

echo "✅ MyGate Flask project structure created successfully!"
