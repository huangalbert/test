from typing import List, Union
from enum import IntEnum, Enum

from pydantic import BaseModel, Field
from decimal import Decimal


class ItemSize(str, Enum):
    S = 'S'
    M = 'M'
    L = 'L'


class ItemColor(str, Enum):
    RED = 'Red'
    BLUE = 'Blue'
    WHITE = 'White'
    GREEN = 'Green'
    BLACK = 'Black'


class ItemCategory(IntEnum):
    CLOTH = 1
    PANTS = 2
    #TODO: etc


class ItemCreate(BaseModel):
    code: str = Field(..., description='item code') 
    name: str = Field(..., description='item nome') 
    category_id: ItemCategory = Field(..., description='category id') 
    inventory: int = Field(..., description='inventory') 
    unit_price: Decimal = Field(..., description='price')
    size: List[ItemSize] = Field(...)
    color: List[ItemColor] = Field(...)


class ItemUpdate(BaseModel):
    name: str = Field(..., description='item nome') 
    category_id: ItemCategory = Field(..., description='category id') 
    inventory: int = Field(..., description='inventory') 
    unit_price: Decimal = Field(..., description='price')


class ItemCategoryCreate(BaseModel):
    id: int = Field(..., description='category id') 
    name: str = Field(..., description='category nome') 

