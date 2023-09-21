from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from datetime import datetime
from .base_class import Base


class User(Base):
    __tablename__: str = "users"

    created_at = Column(
        DateTime, index=True, default=datetime.now, nullable=False
    )
    id_user = Column(
        Integer,
        primary_key=True,
        nullable=False,
        index=True,
        autoincrement=True,
    )
    name_user = Column(String(30), nullable=False, index=False, unique=False)
    email = Column(String, nullable=False, index=True, unique=True)
    favorites = relationship(
        'ProductFavorite', backref='users', lazy='subquery'
    )

    __table_args__ = (PrimaryKeyConstraint(id_user, name="pk_users"),)


class Product(Base):
    __tablename__: str = "products"

    created_at = Column(
        DateTime, index=True, default=datetime.now, nullable=False
    )
    id_product = Column(
        Integer,
        primary_key=True,
        nullable=False,
        index=True,
        autoincrement=True,
    )
    title = Column(String, nullable=False, index=False, unique=False)
    marca = Column(String, nullable=False, index=False, unique=False)
    comentario = Column(String(10), nullable=False, index=False, unique=False)
    description = Column(String(30), nullable=False, index=False, unique=False)

    __table_args__ = (PrimaryKeyConstraint(id_product, name="pk_products"),)


class ProductFavorite(Base):
    __tablename__: str = "favorites"

    created_at = Column(
        DateTime, index=True, default=datetime.now, nullable=False
    )
    id_favorite = Column(
        Integer,
        primary_key=True,
        nullable=False,
        index=True,
        autoincrement=True,
    )
    id_user = Column(Integer, ForeignKey('users.id_user'))  # tabela.campo
    id_product = Column(Integer, ForeignKey('products.id_product'))

    __table_args__ = (PrimaryKeyConstraint(id_favorite, name="pk_favorites"),)
