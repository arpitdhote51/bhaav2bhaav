from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Crop(db.Model):
    __tablename__ = 'crops'
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())
