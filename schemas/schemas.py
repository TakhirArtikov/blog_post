from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    category_id: int
    author_id: int


class AuthorBase(BaseModel):
    name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class PostTag(BaseModel):
    post_id: int
    tag_id: int

    class Config:
        orm_mode = True
