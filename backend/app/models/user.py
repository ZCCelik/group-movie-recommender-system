from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Date
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[Date | None] = mapped_column(Date, nullable=True)