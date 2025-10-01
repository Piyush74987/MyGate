from utils.openai_client import ask_ai

TOOLS = [
    {"name": "approve_visitor", "parameters": {"visitorId": "string"}},
    {"name": "deny_visitor", "parameters": {"visitorId": "string", "reason": "string"}},
    {"name": "checkin_visitor", "parameters": {"visitorId": "string"}},
]

def process_chat(prompt):
    return ask_ai(prompt, tools=TOOLS)
