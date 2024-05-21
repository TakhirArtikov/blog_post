from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db
from models import models, Author
from schemas import schemas

router = APIRouter(tags=["authors"])


@router.post(path="/authors", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(name=author.name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.get(path="/authors", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = db.query(models.Author).offset(skip).limit(limit).all()
    return authors


@router.get("/authors/{author_id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(Author.id == author_id).first()
    if not author:
        return JSONResponse(status_code=404, content={"detail": "Author not found"})
    return author


@router.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, updated_author: schemas.Author, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(Author.id == author_id).first()
    if not author:
        return JSONResponse(status_code=404, content={"detail": "Author not found"})

    author.name = updated_author.name
    author.email = updated_author.email

    db.commit()
    db.refresh(author)
    return author


@router.delete("/authors/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(Author.id == author_id).first()
    if not author:
        return JSONResponse(status_code=404, content={"detail": "Author not found"})

    db.delete(author)
    db.commit()
    return None
