import os
import requests
import time

import jwt
from langchain_community.llms import YandexGPT
from langchain_community.embeddings.yandex import YandexGPTEmbeddings

from app.config import (
    GPT_MODEL_URL,
    EMB_MODEL_URL,
    FOLDER_ID,
    API_URL,
    SERVICE_ACCOUNT_ID,
    PRIVATE_KEY,
    KEY_ID,
)


class YandexGPTConnection:
    def __init__(self):
        self.__get_yandex_token()
        self.llm = YandexGPT(model_uri=GPT_MODEL_URL)
        self.embeddings = YandexGPTEmbeddings(
            model_uri=EMB_MODEL_URL, folder_id=FOLDER_ID
        )

    def __get_yandex_token(self) -> None:
        now = int(time.time())
        payload = {
            "aud": API_URL,
            "iss": SERVICE_ACCOUNT_ID,
            "iat": now,
            "exp": now + 360,
        }

        # Forming JWT
        encoded_token = jwt.encode(
            payload, PRIVATE_KEY, algorithm="PS256", headers={"kid": KEY_ID}
        )

        x = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={"jwt": encoded_token},
        ).json()
        os.environ["YC_IAM_TOKEN"] = x["iamToken"]
