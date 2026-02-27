from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class RoomBase(BaseModel):
    name: Optional[str] = None
    
class RoomCreate(BaseModel):
    name: Optional[str] = None
    

class ParticipantResponse(BaseModel):
    id: str
    nickname: str
    is_ready: bool

    class Config:
        from_attributes = True
        
        
class RoomResponse(BaseModel):
    id: str
    name: Optional[str]
    created_at: datetime
    participants: List[ParticipantResponse] = []

    class Config:
        from_attributes = True
        
        
class JoinRoomRequest(BaseModel):
    nickname: str
    
class JoinRoomResponse(BaseModel):
    participant_id: str
    nickname: str
    
class RatingCreate(BaseModel):
    movie_id: int
    score: float