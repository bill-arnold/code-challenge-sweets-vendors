from app import app
from models import db,Vendor,VendorSweet,Sweet
from datetime import datetime

with app.app_context():
    Vendor = [
        {'name': 'Vendor A'},
        {'name': 'Vendor B'},
        {'name': 'Vendor C'},
        {'name': 'Sweet Delights'},
        {'name': 'Flavor Fusion'},
        {'name': 'Sugar Bliss'},
        {'name': 'Treats Galore'},
        {'name': 'Yummy Creations'},
        {'name': 'Delicious Delicacies'},
        {'name': 'Candy Carnival'},
        {'name': 'Heavenly Treats'},
        {'name': 'Gourmet Sweets'},
        {'name': 'Divine Desserts'},
        {'name': 'Mega Munchies'},
        {'name': 'Sugary Spectacle'},
        {'name': 'Fantastic Flavors'},
        {'name': 'Epicurean Euphoria'},
        {'name': 'Wholesome Treats'},
        {'name': 'Joyful Jellies'},
        {'name': 'Luscious Bites'},
    ]
sweets = [
        {'name': 'Sweet 1'},
        {'name': 'Sweet 2'},
        {'name': 'Sweet 3'},
        {'name': 'ChocoFiesta'},
        {'name': 'Berry Bonanza'},
        {'name': 'Caramel Dream'},
        {'name': 'Mango Magic'},
        {'name': 'Cookie Crunch'},
        {'name': 'Fruity Explosion'},
        {'name': 'Velvet Vanilla'},
        {'name': 'Honey Harmony'},
        {'name': 'Peachy Pleasure'},
        {'name': 'Citrus Celebration'},
        {'name': 'Crunchy Caramel'},
        {'name': 'Cherry Charm'},
        {'name': 'Minty Marvel'},
        {'name': 'Toffee Temptation'},
        {'name': 'Butterscotch Bliss'},
        {'name': 'Coconut Carnival'},
        {'name': 'Almond Delight'},
       
    ]

for vendor_data in vendors:
        vendor = Vendor(**vendor_data)
        db.session.add(vendor)
db.session.commit()
print("🍭 Vendors seeded!")

    
for sweet_data in sweets:
        sweet = Sweet(**sweet_data)
        db.session.add(sweet)
db.session.commit()
print("🍬 Sweets seeded!")
