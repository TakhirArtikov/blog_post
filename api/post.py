from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db
from models import models,Post
from schemas import schemas
router = APIRouter(tags=["posts"])


@router.get("/posts", response_model=List[schemas.Post])
def get_all_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.Post).all()
    return all_posts


@router.post("/posts", response_model=schemas.Post, status_code=201)
def create_post(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/posts/{post_id}", response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(Post.id == post_id).first()
    if not post:
        return JSONResponse(status_code=404, content={"detail": "Post not found"})
    return post


@router.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, updated_post: schemas.Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(Post.id == post_id).first()
    if not post:
        return JSONResponse(status_code=404, content={"detail": "Post not found"})

    post.title = updated_post.title
    post.content = updated_post.content
    post.author_id = updated_post.author_id
    post.category_id = updated_post.category_id

    db.commit()
    db.refresh(post)
    return post


@router.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(Post.id == post_id).first()
    if not post:
        return JSONResponse(status_code=404, content={"detail": "Post not found"})

    db.delete(post)
    db.commit()
    return None
