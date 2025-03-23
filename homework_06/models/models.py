"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimeStamp

if TYPE_CHECKING:
    from . import Post
    
class User(TimeStamp, Base):
    
    username: Mapped[str] = mapped_column( # Уникальный username
        String(100),
        nullable=False,
        unique=True
    )
    email: Mapped[str] = mapped_column( # Почтовый адрес
        String(150),
        nullable=True, # При регистрации можем не указывать email, но в последствии должен быть подтвержден
        unique=True,
    )
    firstName: Mapped[str] = mapped_column( # Имя
        String(150),
        nullable=True,
        unique=False,
    )
    lastName: Mapped[str] = mapped_column( # Фамилия
        String(150),
        nullable=True,
        unique=False,
    )
    age: Mapped[int] = mapped_column( # Возраст
        Integer,
        nullable=True,
        unique=False
    )
    gender: Mapped[str] = mapped_column( # Пол
        String(50),
        nullable=True,
        unique=False
    )
    
    posts: Mapped[list["Post"]] = relationship(back_populates="user") # Отношение one-to-many к модели Post
    
    def __str__(self):
        return f"{self.__class__.__name__} №{self.id}. {self.username} ({self.firstName} {self.lastName})"
    
class Post(TimeStamp, Base):
    __tablename__ = 'post'
    
    title: Mapped[str] = mapped_column( # Заголовок
        String(100),
        unique=False,
        nullable=False
    )
    
    body: Mapped[str] = mapped_column( # Содержимое
        Text,
        default="",
        server_default="",
    )
    
    views: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )
    
    userId: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False) # Внешний ключ, ссылающийся на таблицу User
    user: Mapped["User"] = relationship(back_populates="posts")                # Отношение many-to-one к модели User
    
    def __str__(self):
        return f"{self.__class__.__name__} №{self.id} (user_id: {self.userId}). {self.title}"