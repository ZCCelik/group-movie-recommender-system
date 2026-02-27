from sqlalchemy.orm import Session
import app.database.room_crud as crud
import app.schemas.room as schema
from fastapi import HTTPException


def create_room(db: Session, payload: schema.RoomCreate): 
    return crud.create_room(db, payload)

def get_room_by_id(db: Session, room_id: str):
    room = crud.get_room_by_id(db, room_id)
    
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

def join_room(db: Session, room_id: str, nickname: str):
    room = crud.get_room(db, room_id)

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    if room.is_locked:
        raise HTTPException(status_code=403,detail="Room is locked. You cannot join anymore.")

    return crud.create_participant(db, room_id, nickname)