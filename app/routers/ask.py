from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, models, database
from .dependencies import get_db
import openai

router = APIRouter()

@router.post("/ask", response_model=schemas.AskResponse)
def ask_question(request: schemas.AskRequest, db: Session = Depends(get_db)):
    openai.api_key = "your_openai_api_key"
    response = openai.Completion.create(
        engine="davinci",
        prompt=request.question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    crud.create_user_interaction(db=db, interaction=request, response=answer)
    return schemas.AskResponse(response=answer)