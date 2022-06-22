from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/{item_code}")#, response_model=schemas.User)
def read_item(item_code: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, code=item_code)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@app.post("/categories/")#, response_model=schemas.User)
def create_items(category: schemas.ItemCategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, email=category.id)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return crud.create_category(db=db, category=category)


@app.post("/items/")#, response_model=schemas.User)
def create_items(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, code=item.code)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered")
    return crud.create_item(db=db, item=item)


@app.patch("/items/{item_code}")#, response_model=schemas.User)
def patch_items(item_code: str, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, code=item_code)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return crud.patch_item(db=db, item=db_item[0], item_update=item_update)


@app.delete("/items/{item_code}")#, response_model=schemas.User)
def delete_items(item_code: str, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, code=item_code)
    if not db_item:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_item(db=db, item=db_item)
