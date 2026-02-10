from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, Date
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[Date | None] = mapped_column(Date, nullable=True)
    
    groups: Mapped[list["Group"]] = relationship(
        secondary="group_members", 
        back_populates="members"
    )