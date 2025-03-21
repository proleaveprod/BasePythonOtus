from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime

from config.config import convention

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class TimeStamp:
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        # default=func.now(),
        server_default=func.now(),
        nullable=False,
    )