import sqlalchemy.orm as orm
import sqlalchemy as sa
from datetime import datetime

Base = orm.declarative_base()

class User(Base):
    __tablename__: str ="users"

    created_at = sa.Column(sa.DateTime, index=True, default=datetime.now, nullable=False)
    id_user = sa.Column(sa.Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name_user = sa.Column(sa.String(30), nullable=False, index=True, unique=False)
    email = sa.Column(sa.String, nullable=False, index=True, unique=True)
    favorites = orm.relationship('ProductFavorite', backref='users', lazy='subquery')

    __table_args__ = (sa.PrimaryKeyConstraint(id_user, name="pk_users"),)

class Product(Base):
    __tablename__: str = "products"

    created_at = sa.Column(sa.DateTime, index=True, default=datetime.now, nullable=False)
    id_product = sa.Column(sa.Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, index=True, unique=False)
    marca = sa.Column(sa.String, nullable=False, index=True, unique=False)
    description = sa.Column(sa.String(30), nullable=False, index=True, unique=False)

    __table_args__ = (sa.PrimaryKeyConstraint(id_product, name="pk_products"),)

class ProductFavorite(Base):
    __tablename__: str = "favorites"

    created_at = sa.Column(sa.DateTime, index=True, default=datetime.now, nullable=False)
    id_favorite = sa.Column(sa.Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    id_user = sa.Column(sa.Integer, sa.ForeignKey('users.id_user')) # tabela.campo
    id_product = sa.Column(sa.Integer, sa.ForeignKey('products.id_product'))
  
    __table_args__ = (sa.PrimaryKeyConstraint(id_favorite, name="pk_favorites"),)