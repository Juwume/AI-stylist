from sqlalchemy import Column, Integer, String, Text
from .database import Base

class UserInteraction(Base):
    __tablename__ = "user_interactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    question = Column(Text, nullable=False)
    response = Column(Text, nullable=False)