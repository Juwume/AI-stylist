from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class ConversationRequest(BaseModel):
    user_id: str
    conversation_id: str | None = None
    message: str
    image_url: Optional[HttpUrl] = Field(
        None, description="URL of the image to include in the prompt"
    )


class ConversationResponse(BaseModel):
    conversation_id: str
    response_text: str
