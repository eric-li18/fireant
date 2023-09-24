from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from .util import get_db

router = APIRouter()


@router.get("/{item_id}/", response_model=schemas.Bug)
def get_bug(
    db: Session = Depends(get_db),
    item_id: int = Path(..., title="ID of bug to get", ge=1),
):
    item = crud.bug.get(db, item_id)
    if not item:
        raise HTTPException(
            status_code=404, detail=f"Bug with id: {item_id} not found."
        )
    return item


@router.get("/", response_model=List[schemas.Bug])
def get_bugs(
    db: Session = Depends(get_db),
    limit: int = Query(None, title="Upper limit of records returned", ge=1),
):
    items = crud.bug.get_multi(db, limit)
    if not items:
        raise HTTPException(status_code=404, detail=f"Database is empty.")
    return items
