import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(prompt, tools=None):
    """
    Wrapper for OpenAI tool-calling (chat with function calling)
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
    )
    return response
