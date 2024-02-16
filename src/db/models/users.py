import datetime

from sqlalchemy import ForeignKey, String, Column, Integer, TIMESTAMP, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base import BaseModel
from src.db.models.roles import Role


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = Column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow)
    role_id: Mapped[Role] = Column(Integer, ForeignKey("roles.id"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    def __repr__(self):
        return (
            f'<User id={self.id},'
            f' email={self.email},'
            f' first_name={self.username}'
        )
