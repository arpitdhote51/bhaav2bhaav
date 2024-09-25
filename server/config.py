import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/market_price_tracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
