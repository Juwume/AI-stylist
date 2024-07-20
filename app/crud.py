from sqlalchemy.orm import Session
from . import models, schemas

def create_user_interaction(db: Session, interaction: schemas.AskRequest, response: str):
    db_interaction = models.UserInteraction(user_id=interaction.user_id, question=interaction.question, response=response)
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction