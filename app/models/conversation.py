from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class ConversationRequest(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    conversation_id: Optional[str] = Field(
        None, description="Unique identifier for the conversation"
    )
    message: str = Field(..., description="User's message text")
    image_url: Optional[HttpUrl] = Field(
        None, description="URL of the image to include in the prompt"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "<id-example>",
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "message": "Give me style advices, based on my look pls",
                "image_url": "http://example.com/image.jpg",
            }
        }


class ConversationResponse(BaseModel):
    conversation_id: str = Field(
        ..., description="Unique identifier for the conversation"
    )
    response_text: str = Field(..., description="Response text from the server")

    class Config:
        json_schema_extra = {
            "example": {
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "response_text": "The combination of the peach top and the iridescent sequined overlay makes it a standout piece.",
            }
        }
