from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, models, database
from .dependencies import get_db
import openai

router = APIRouter()

@router.post("/suggest", response_model=schemas.SuggestResponse)
def suggest_outfit(request: schemas.SuggestRequest, db: Session = Depends(get_db)):
    openai.api_key = "your_openai_api_key"
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Suggest an outfit for someone with the following preferences: {request.style_preferences}",
        max_tokens=150
    )
    suggestions = response.choices[0].text.strip()
    crud.create_user_interaction(db=db, interaction=request, response=suggestions)
    return schemas.SuggestResponse(suggestions=suggestions)