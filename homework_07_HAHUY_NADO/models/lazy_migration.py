from .base import Base, engine

def migrate():
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    