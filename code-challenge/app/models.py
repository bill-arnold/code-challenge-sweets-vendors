from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Vendor(db.Model, ):
    __tablename__ = 'vendor'

    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(255), nullable=False)
    create_at=db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at=db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='vendor')

class Sweet(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='sweet')

class VendorSweet(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    vendor = db.relationship('Vendor', back_populates='vendor_sweets')
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')

# adding validation for the vendor sweet model
@db.validates('price')
def validate_price(self,key,price):
    if not price:
        raise ValueError('Price cannot be blank')
    if price<0:
        raise ValueError("Price can't be negative number")
    return price