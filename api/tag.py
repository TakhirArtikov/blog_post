from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db
from models import models,Tag
from schemas import schemas
router = APIRouter(tags=["tags"])


@router.get("/tags", response_model=List[schemas.Tag])
def get_all_tags(db: Session = Depends(get_db)):
    all_tags = db.query(models.Tag).all()
    return all_tags


@router.get("/tags/{tag_id}", response_model=schemas.Tag)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(Tag.id == tag_id).first()
    if not tag:
        return JSONResponse(status_code=404, content={"detail": "Tag not found"})
    return tag


@router.post("/tags", response_model=schemas.Tag, status_code=201)
def create_tag(tag: schemas.Tag, db: Session = Depends(get_db)):
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.put("/tags/{tag_id}", response_model=schemas.Tag)
def update_tag(tag_id: int, updated_tag: schemas.Tag, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(Tag.id == tag_id).first()
    if not tag:
        return JSONResponse(status_code=404, content={"detail": "Tag not found"})

    tag.name = updated_tag.name

    db.commit()
    db.refresh(tag)
    return tag


@router.delete("/tags/{tag_id}", status_code=204)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(Tag.id == tag_id).first()
    if not tag:
        return JSONResponse(status_code=404, content={"detail": "Tag not found"})

    db.delete(tag)
    db.commit()
    return None
