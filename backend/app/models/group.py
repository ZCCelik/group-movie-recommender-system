from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Table, ForeignKey, Date, Column
from app.database.base import Base

group_members = Table(
    "group_members",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("group.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "user_id",
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

class Group(Base): 
    __tablename__ = "groups"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))