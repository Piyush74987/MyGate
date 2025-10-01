from firebase_admin import auth

def set_custom_claims(uid, role):
    """Assign role to user (admin/guard/resident)."""
    auth.set_custom_user_claims(uid, {"role": role})

def get_user_role(decoded_token):
    return decoded_token.get("role", None)

def is_authorized(user_role, action):
    """Basic RBAC check."""
    rules = {
        "resident": ["create_visitor", "approve_visitor", "deny_visitor"],
        "guard": ["checkin_visitor", "checkout_visitor"],
        "admin": ["*"]
    }
    return "*" in rules.get(user_role, []) or action in rules.get(user_role, [])
