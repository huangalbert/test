from sqlalchemy import Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Item(Base):
    __tablename__ = "item"

    code = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey("item_category.id"), nullable=False, index=True)
    inventory = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(15, 6), nullable=False, index=True)
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now(), comment='資料建置時間')
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), comment='資料建置時間')

    category = relationship("ItemCategory", back_populates="item")
    size = relationship("ItemSize", back_populates="item")
    color = relationship("ItemColor", back_populates="item")

class ItemCategory(Base):
    __tablename__ = "item_category"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), comment='資料建置時間')

    item = relationship("Item", back_populates="category")

class ItemSize(Base):
    __tablename__ = 'item_size'

    item_code = Column(String, ForeignKey("item.code"), index=True)
    size = Column(String(20), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), comment='資料建置時間')

    __table_args__ =(PrimaryKeyConstraint("item_code", "size"),)

    item = relationship("Item", back_populates="size")


class ItemColor(Base):
    __tablename__ = 'item_color'

    item_code = Column(String, ForeignKey("item.code"), index=True)
    color = Column(String(20), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), comment='資料建置時間')

    __table_args__ = (PrimaryKeyConstraint("item_code", "color"),)

    item = relationship("Item", cascade='all,delete', back_populates="color")
