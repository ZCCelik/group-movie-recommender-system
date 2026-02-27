from sqlalchemy.orm import Session
import app.schemas.room as schema
from app.models.room import Room
from app.models.participant import Participant

def create_room(db: Session, payload: schema.RoomCreate) -> Room:
    room = Room(name=payload.name)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def get_room_by_id(db: Session, room_id: str) -> Room | None:
    stmt = db.select(Room).where(Room.id == room_id).options(db.selectinload(Room.participants))
    return db.scalar(stmt)

def join_room(db: Session, room_id: str, nickname: str):
    participant = Participant(nickname=nickname, room_id=room_id)
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant