from sqlalchemy import (
    Column,
    MetaData,
)
from sqlalchemy import Integer
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)


class Base(DeclarativeBase):

    # metadata = MetaData(naming_convention={
    #     # "ix": "ix_%(column_0_label)s",
    #     # "uq": "uq_%(table_name)s_%(column_0_name)s",
    #     # "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    #     # "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    #     # "pk": "pk_%(table_name)s",
    # })


    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)