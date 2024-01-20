#!/usr/bin/env python3

from flask import Flask, jsonify,request
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse, abort
from models import db, Vendor, VendorSweet, Sweet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class VendorResource(Resource):
    def get(self):
        vendors = Vendor.query.all()
        response = [vendor.to_dict() for vendor in vendors]
        return response

class VendorByIdResource(Resource):
    def get(self, vendor_id):
        vendor = Vendor.query.get(vendor_id)
        if vendor is None:
            return {"error": "Vendor not found"}, 404

        return vendor.to_dict()
    
class SweetsResource(Resource):
    def get(self):
        sweets = Sweet.query.all()
        response = [sweet.to_dict() for sweet in sweets]
        return response

class SweetByIdResource(Resource):
    def get(self, sweet_id):
        sweet = Sweet.query.get(sweet_id)
        if sweet is None:
            return {"error": "Sweet not found"}, 404

        return sweet.to_dict()

    

    

api.add_resource(VendorResource, '/vendors')
api.add_resource(VendorByIdResource, '/vendors/<int:vendor_id>')
api.add_resource(SweetsResource, '/sweets')
api.add_resource(SweetByIdResource, '/sweets/<int:sweet_id>')


if __name__ == '__main__':
    app.run(port=5555)
