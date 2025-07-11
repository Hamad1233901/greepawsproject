from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    cnic = db.Column(db.String(20))

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(50))
    dob = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    owner = db.relationship('Client', backref=db.backref('pets', lazy=True))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "GreenPaws backend is running."

@app.route('/api/clients', methods=['GET', 'POST'])
def manage_clients():
    if request.method == 'POST':
        data = request.json
        client = Client(name=data['name'], phone=data['phone'], cnic=data.get('cnic', ''))
        db.session.add(client)
        db.session.commit()
        return jsonify({'message': 'Client added'}), 201

    clients = Client.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'phone': c.phone,
        'cnic': c.cnic
    } for c in clients])

@app.route('/api/clients/<int:id>', methods=['PUT'])
def update_client(id):
    client = Client.query.get_or_404(id)
    data = request.json
    client.name = data['name']
    client.phone = data['phone']
    client.cnic = data.get('cnic', '')
    db.session.commit()
    return jsonify({'message': 'Client updated'})

@app.route('/api/pets', methods=['POST', 'GET'])
def manage_pets():
    if request.method == 'POST':
        data = request.json
        pet = Pet(
            name=data['name'],
            species=data['species'],
            breed=data.get('breed', ''),
            dob=data.get('dob', ''),
            owner_id=data['owner_id']
        )
        db.session.add(pet)
        db.session.commit()
        return jsonify({'message': 'Pet added'}), 201

    pets = Pet.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'species': p.species,
            'breed': p.breed,
            'dob': p.dob,
            'owner_id': p.owner_id
        }
        for p in pets
    ])

if __name__ == '__main__':
    app.run(debug=True)
