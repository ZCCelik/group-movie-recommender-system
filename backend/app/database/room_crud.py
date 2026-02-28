from itertools import count

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

def get_participant_in_room(db: Session, room_id: int, participant_id: int):
    stmt = db.select(Participant).where(
        Participant.id == participant_id,
        Participant.room_id == room_id
    )
    return db.execute(stmt).scalar_one_or_none()

def set_participant_ready(db: Session, participant: Participant):
    participant.is_ready = True
    db.commit()
    db.refresh(participant)
    return participant

def count_not_ready(db: Session, room_id: int):
    stmt = db.select(count()).select_from(Participant).where(
        Participant.room_id == room_id,
        Participant.is_ready == False
    )
    return db.execute(stmt).scalar_one()

def lock_room(db: Session, room_id: int):
    stmt = db.select(Room).where(Room.id == room_id)
    room = db.execute(stmt).scalar_one_or_none()

    if room:
        room.is_locked = True
        db.commit()
        db.refresh(room)

    return room