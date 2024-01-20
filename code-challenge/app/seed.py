from app import app
from models import db, Vendor, Sweet, VendorSweet
from datetime import datetime

with app.app_context():
    # Vendors data
    vendors = [
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

    # Sweets data
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
        # ... Add more sweets
    ]

    # VendorSweets data
    vendor_sweets = [
        {'vendor_id': 1, 'sweet_id': 1, 'price': 200},
        {'vendor_id': 1, 'sweet_id': 2, 'price': 300},
        {'vendor_id': 2, 'sweet_id': 3, 'price': 250},
        {'vendor_id': 2, 'sweet_id': 4, 'price': 180},
        {'vendor_id': 3, 'sweet_id': 5, 'price': 220},
        {'vendor_id': 3, 'sweet_id': 6, 'price': 350},
        {'vendor_id': 4, 'sweet_id': 7, 'price': 280},
        {'vendor_id': 4, 'sweet_id': 8, 'price': 200},
        {'vendor_id': 5, 'sweet_id': 9, 'price': 300},
        {'vendor_id': 5, 'sweet_id': 10, 'price': 240},
        {'vendor_id': 6, 'sweet_id': 11, 'price': 260},
        {'vendor_id': 6, 'sweet_id': 12, 'price': 320},
        {'vendor_id': 7, 'sweet_id': 13, 'price': 180},
        {'vendor_id': 7, 'sweet_id': 14, 'price': 300},
        {'vendor_id': 8, 'sweet_id': 15, 'price': 250},
        {'vendor_id': 8, 'sweet_id': 16, 'price': 280},
        {'vendor_id': 9, 'sweet_id': 17, 'price': 220},
        {'vendor_id': 9, 'sweet_id': 18, 'price': 320},
        {'vendor_id': 10, 'sweet_id': 19, 'price': 280},
        {'vendor_id': 10, 'sweet_id': 20, 'price': 200},
        # ... Add more vendor_sweets
    ]

    # Seed vendors
    for vendor_data in vendors:
        vendor = Vendor(**vendor_data)
        db.session.add(vendor)

    db.session.commit()
    print("🍭 Vendors seeded!")

    # Seed sweets
    for sweet_data in sweets:
        sweet = Sweet(**sweet_data)
        db.session.add(sweet)

    db.session.commit()
    print("🍬 Sweets seeded!")

    # Seed vendor_sweets
    for vs_data in vendor_sweets:
        vendor_sweet = VendorSweet(**vs_data)
        db.session.add(vendor_sweet)

    db.session.commit()
    print("🍭 VendorSweets seeded!")
