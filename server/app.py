from flask import Flask, jsonify, request
from models import db, Crop
from market_price_tracker.server.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Route to get all crops
@app.route('/crops', methods=['GET'])
def get_crops():
    crops = Crop.query.all()
    return jsonify([{
        'id': crop.id,
        'name': crop.crop_name,
        'price': str(crop.price),
        'updated_at': crop.updated_at
    } for crop in crops])

# Route to add a new crop price
@app.route('/crops', methods=['POST'])
def add_crop():
    data = request.get_json()
    new_crop = Crop(crop_name=data['name'], price=data['price'])
    db.session.add(new_crop)
    db.session.commit()
    return jsonify({'message': 'Crop added successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
