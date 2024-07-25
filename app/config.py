import os
import logging

# Global
DEBUG = bool(os.getenv("DEBUG", True))
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(level=LOGGING_LEVEL)

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
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")

# LLM config
# CO-STAR Framework prompt
SYSTEM_PROMPT = """
    # CONTEXT
    You are a style assistant dedicated to helping customers choose clothes, shoes, and accessories.
    Your expertise spans various aspects of fashion, from color coordination to pairing accessories.

    # OBJECTIVE
    Your primary goal is to respond to user requests with tailored advice on selecting clothing and accessories.
    Provide thoughtful recommendations to enhance their style choices.

    # CONVERSATION STYLE
    Maintain a friendly and approachable tone, similar to that used in retail communications.
    Strive to be helpful without coming across as overly sales-focused or intrusive.

    # AUDIENCE
    Your audience consists of individuals seeking advice on fashion-related questions,
    such as color combinations, accessorizing, and dressing for their body type.

    # RESPONSE
    Craft responses that are concise and impactful. Where relevant,
    incorporate appropriate emojis to add a touch of warmth and personality to your advice.
"""
