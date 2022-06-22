from unicodedata import category
from sqlalchemy.orm import Session, contains_eager

from . import models, schemas


def get_item(db: Session, code: str):
    return db.query(models.Item). \
        filter(models.Item.code == code). \
        outerjoin(models.Item.size). \
        options(contains_eager(models.Item.size)). \
        outerjoin(models.Item.color). \
        options(contains_eager(models.Item.color)). \
        all()

def get_category(db: Session, id: int):
    return db.query(models.ItemCategory).filter(models.ItemCategory.id == id).first()

def create_category(db: Session, category: schemas.ItemCategoryCreate):
    db_category = models.ItemCategory(id=category.id, name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        code=item.code ,
        name=item.name ,
        category_id = item.category_id,
        inventory = item.inventory,
        unit_price = item.unit_price
        )
    
    for size in item.size:
        new_size = models.ItemSize(item_code=item.code, size=size)
        db_item.size.append(new_size)

    for color in item.color:
        new_color = models.ItemColor(item_code=item.code, color=color)
        db_item.color.append(new_color) 

    db.add(db_item)    
    db.commit()
    db.refresh(db_item)
    return db_item

def patch_item(db: Session, item: models.Item, item_update: schemas.ItemUpdate):
    item.name = item_update.name
    item.category_id = item_update.category_id
    item.inventory = item_update.inventory
    item.unit_price = item_update.unit_price

    db.add(item)
    db.commit()
    return item

def delete_item(db: Session, db_item: models.Item):
    for i in db_item.size:
        db.delete(i)
    for i in db_item.color:
        db.delete(i) 
    db.delete(db_item)
    db.commit()


