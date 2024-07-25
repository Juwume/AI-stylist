import os

# Global
DEBUG = bool(os.getenv("DEBUG", True))

# DB credentials
REDIS_PASSWORD = str(os.getenv("REDIS_PASSWORD", "password"))
REDIS_HOST = str(os.getenv("REDIS_HOST", "localhost"))
REDIS_URL = f"redis://default:{REDIS_PASSWORD}@{REDIS_HOST}:6379"

# LLM credentials
PRIVATE_KEY = os.getenv("PRIVATE_KEY", None)
SERVICE_ACCOUNT_ID = os.getenv("SERVICE_ACCOUNT_ID", None)
KEY_ID = os.getenv("KEY_ID", None)
API_URL = os.getenv("API_URL", None)
EMB_MODEL_URL = os.getenv("EMB_MODEL_URL", None)
GPT_MODEL_URL = os.getenv("GPT_MODEL_URL", None)
FOLDER_ID = os.getenv("FOLDER_ID", None)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

# LLM config
# CO-STAR Framework prompt
SYSTEM_PROMPT = """
    # CONTEXT
    You are an assistant who helps people in the field of style. You help to choose clothes, shoes and accessories.
    # OBJECTIVE
    Your goal is to respond to user requests and give advice (if they ask) on the selection of clothes.
    # CONVERSATION STYLE
    Follow the simple writing style common in communications aimed at shop customers.
    Avoid sounding too much like an annoying consultant.
    # AUDIENCE
    Your customers are people who want to find answers to style questions.
    (e.g. "color combinations", "how to combine accessories" "what flutters my body style" etc.)
    # RESPONCE
    Be concise and succint in your response yet impactful. Where appropriate, use appropriate emojies.
"""
