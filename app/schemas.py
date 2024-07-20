from pydantic import BaseModel

class AskRequest(BaseModel):
    user_id: str
    question: str

class AskResponse(BaseModel):
    response: str

class SuggestRequest(BaseModel):
    user_id: str
    style_preferences: str

class SuggestResponse(BaseModel):
    suggestions: str