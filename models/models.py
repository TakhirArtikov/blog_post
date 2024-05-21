from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship

from models.base import BaseModel


class PostsTags(BaseModel):
    __tablename__ = "posts_tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))


class Post(BaseModel):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    author = relationship("Author", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    tags = relationship("Tag", secondary="posts_tags", back_populates="posts")


class Category(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    posts = relationship("Post", back_populates="category")


class Tag(BaseModel):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    posts = relationship("Post", secondary='posts_tags', back_populates="tags")


class Author(BaseModel):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

    posts = relationship("Post", back_populates="author")
