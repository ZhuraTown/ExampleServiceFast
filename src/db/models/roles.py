from sqlalchemy import String, Column, Integer,JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    permissions: Mapped[dict] = Column(
        JSON,
        nullable=False
    )

