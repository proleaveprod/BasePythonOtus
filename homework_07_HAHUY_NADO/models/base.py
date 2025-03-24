#Globals
from sqlalchemy import MetaData, create_engine,  DateTime, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, Session
from datetime import datetime
from enum import Enum
#Locals
from config import convention, db_url, db_echo

engine = create_engine(url=db_url, echo=db_echo)

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class CreatedTimeStamp:
    created: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )
