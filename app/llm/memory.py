import openai
import base64
from langchain_community.chat_message_histories import RedisChatMessageHistory
from app.config import SYSTEM_PROMPT, REDIS_URL, OPENAI_API_KEY, OPENAI_MODEL_NAME


class ChatMemory:
    """
    A class to handle chat memory and interaction with OpenAI's API, utilizing Redis for message history storage.

    Attributes:
        redis_url (str): The URL for connecting to the Redis instance.
        client (openai.Client): The OpenAI client initialized with the provided API key.
    """

    def __init__(self, redis_url: str, openai_api_key: str):
        """
        Initializes the ChatMemory instance with Redis URL and OpenAI API key.

        Args:
            redis_url (str): The URL for connecting to the Redis instance.
            openai_api_key (str): The API key for accessing OpenAI services.
        """
        self.redis_url = redis_url
        self.client = openai.OpenAI(api_key=openai_api_key)

    def get_message_history(self, session_id: str) -> RedisChatMessageHistory:
        """
        Retrieves the chat message history for a given session ID from Redis.

        Args:
            session_id (str): The unique identifier for the chat session.

        Returns:
            RedisChatMessageHistory: The chat message history object for the session.
        """
        return RedisChatMessageHistory(session_id, url=self.redis_url)

    def invoke(self, session_id: str, message: str, image_data: bytes = None) -> str:
        """
        Processes a user's message, optionally with an image, and gets a response from OpenAI's API.

        Args:
            session_id (str): The unique identifier for the chat session.
            message (str): The user's message text.
            image_data (bytes, optional): The image data in bytes to be included in the prompt.

        Returns:
            str: The response text from OpenAI's API.
        """
        message_history = self.get_message_history(session_id)

        # Handling system prompt initialization
        system_prompt = {
            "role": "system",
            "content": [{"type": "text", "text": SYSTEM_PROMPT}],
        }
        if len(message_history.messages) == 0:
            message_history.add_user_message(str(system_prompt))

        messages_to_api = []

        # Preparing message history for the API request
        for msg in message_history.messages:
            msg = eval(msg.content)
            messages_to_api.append({"role": msg["role"], "content": msg["content"]})

        # Handling the user's query with optional image data
        if image_data:
            image_b64 = base64.b64encode(image_data).decode("utf-8")
            user_query = {
                "role": "user",
                "content": [
                    {"type": "text", "text": message},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                    },
                ],
            }
        else:
            user_query = {
                "role": "user",
                "content": [{"type": "text", "text": message}],
            }
        messages_to_api.append(user_query)

        # Making the API call to OpenAI
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL_NAME, messages=messages_to_api
        )
        response_msg = {
            "role": "assistant",
            "content": [
                {"type": "text", "text": str(response.choices[0].message.content)}
            ],
        }

        # Updating message history with the user's query and API response
        message_history.add_user_message(str(user_query))
        message_history.add_user_message(str(response_msg))

        return str(response.choices[0].message.content)


# Initialize the ChatMemory instance with Redis URL and OpenAI API key
chat_memory = ChatMemory(REDIS_URL, OPENAI_API_KEY)
