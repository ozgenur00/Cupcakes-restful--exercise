from app import app
from models import db, Cupcake

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Cupcake(flavor="cherry", size="large", rating=5)
    c2 = Cupcake(flavor="chocolate", size="small", rating=9, image="https://example.com/image.jpg")

    db.session.add_all([c1, c2])
    db.session.commit()