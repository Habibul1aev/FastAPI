from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.services.category_service import CategoryServise
from app.schemas.category import CategoryResponse


router = APIRouter(
    prefix='/api/v1/categories',
    tags=['categories']
)

@router.get('', response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    service = CategoryServise(db)
    return service.get_all_categories()

@router.get('/{category_id}', response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category(category_id: int, db:Session = Depends(get_db)):
    service = CategoryServise(db)
    return service.get_category_by_id(category_id)