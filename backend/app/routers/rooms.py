from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
import app.schemas.room as schema
import app.services.room_service as service


router = APIRouter(prefix="/rooms")

@router.post("", response_model=schema.RoomCreate)
def create_room(payload: schema.RoomCreate, db: Session = Depends(get_db)): 
    return service.create_room(db, payload)

@router.get("/{room_id}", response_model=schema.RoomResponse)
def get_room_by_id(room_id: str, db: Session = Depends(get_db)):
    return service.get_room_by_id(db, room_id)

@router.post("/{room_id}/join", response_model=schema.JoinRoomResponse)
def join_room(room_id: str, payload: schema.JoinRoomRequest, db: Session = Depends(get_db)):
    return service.join_room(db, room_id, payload.nickname)

@router.post("/{room_id}/participants/{participant_id}/ready", response_model=schema.RoomResponse)
def mark_ready(room_id: str, participant_id: str, db: Session = Depends(get_db)):
    return service.mark_ready(db, room_id, participant_id)