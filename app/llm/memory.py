import openai
import base64
from langchain_community.chat_message_histories import RedisChatMessageHistory
from app.config import SYSTEM_PROMPT, REDIS_URL, OPENAI_API_KEY


class ChatMemory:
    def __init__(self, redis_url: str, openai_api_key: str):
        self.redis_url = redis_url
        self.client = openai.OpenAI(api_key=openai_api_key)

    def get_message_history(self, session_id: str) -> RedisChatMessageHistory:
        return RedisChatMessageHistory(session_id, url=self.redis_url)

    def invoke(self, session_id: str, message: str, image_data: bytes = None) -> str:
        message_history = self.get_message_history(session_id)

        # Handling system prompt
        system_prompt = {
            "role": "system",
            "content": [{"type": "text", "text": SYSTEM_PROMPT}],
        }
        if len(message_history.messages) == 0:
            message_history.add_user_message(str(system_prompt))

        messages_to_api = []

        for msg in message_history.messages:
            msg = eval(msg.content)
            messages_to_api.append({"role": msg["role"], "content": msg["content"]})

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

        response = self.client.chat.completions.create(
            model="gpt-4o-mini", messages=messages_to_api
        )
        response_msg = {
            "role": "assistant",
            "content": [
                {"type": "text", "text": str(response.choices[0].message.content)}
            ],
        }
        message_history.add_user_message(str(user_query))
        message_history.add_user_message(str(response_msg))
        print(message_history.messages)

        return str(response.choices[0].message.content)

    def to_json(self) -> dict:
        return self.chat_api.to_json()


chat_memory = ChatMemory(REDIS_URL, OPENAI_API_KEY)
