#!/usr/bin/env python3

from flask import Flask, jsonify
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
        if vendor:
            return vendor.to_dict()
        else:
            abort(404, error="Vendor not found")

    def patch(self, vendor_id):
        # Add logic to update a vendor
        pass

    def delete(self, vendor_id):
        vendor = Vendor.query.get(vendor_id)
        if vendor:
            db.session.delete(vendor)
            db.session.commit()
            return jsonify({"message": f"Vendor with id {vendor_id} deleted successfully"})
        else:
            abort(404, error="Vendor not found")

# Routes
api.add_resource(VendorResource, '/vendors')
api.add_resource(VendorByIdResource, '/vendors/<int:vendor_id>')

if __name__ == '__main__':
    app.run(port=5555)
