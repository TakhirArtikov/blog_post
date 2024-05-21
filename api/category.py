from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db
from schemas import schemas
from models import models, Category

router = APIRouter(tags=["categories"])


@router.get("/categories", response_model=List[schemas.Category])
def get_all_categories(db: Session = Depends(get_db)):
    all_categories = db.query(models.Category).all()
    return all_categories


@router.get("/categories/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(Category.id == category_id).first()
    if not category:
        return JSONResponse(status_code=404, content={"detail": "Category not found"})
    return category


@router.post("/categories", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.Category, db: Session = Depends(get_db)):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, updated_category: schemas.Category, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(Category.id == category_id).first()
    if not category:
        return JSONResponse(status_code=404, content={"detail": "Category not found"})

    category.name = updated_category.name
    category.description = updated_category.description

    db.commit()
    db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(Category.id == category_id).first()
    if not category:
        return JSONResponse(status_code=404, content={"detail": "Category not found"})

    db.delete(category)
    db.commit()
    return None
