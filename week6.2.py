from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy # type: ignore


app = Flask(__name__)

import os
basedir = os.path.abspath(os.path.dirname(__file__))  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'items.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('week6.2.html')

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully', 'item': {'id': new_item.id, 'name': new_item.name, 'description': new_item.description}}), 201

@app.route('/api/items', methods=['GET'])
def list_items():
    items = Item.query.all()
    items_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(items_list), 200

if __name__ == '__main__':
    app.run(debug=True)