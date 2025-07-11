from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# ----------------------------
# Models
# ----------------------------

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


class VisitRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    next_visit = db.Column(db.String(20))

    pet = db.relationship('Pet', backref=db.backref('visits', lazy=True))


# ----------------------------
# Create database tables
# ----------------------------
with app.app_context():
    db.create_all()


# ----------------------------
# Routes
# ----------------------------

@app.route('/')
def home():
    return "GreenPaws backend is running."


# -------- Clients --------
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


@app.route('/api/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted'})


# -------- Pets --------
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
            'owner_id': p.owner_id,
            'owner_name': p.owner.name
        }
        for p in pets
    ])


@app.route('/api/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    pet = Pet.query.get_or_404(id)
    data = request.json
    pet.name = data['name']
    pet.species = data['species']
    pet.breed = data.get('breed', '')
    pet.dob = data.get('dob', '')
    pet.owner_id = data['owner_id']
    db.session.commit()
    return jsonify({'message': 'Pet updated'})


@app.route('/api/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': 'Pet deleted'})


# -------- Visit Records --------
@app.route('/api/visits', methods=['POST', 'GET'])
def manage_visits():
    if request.method == 'POST':
        data = request.json
        visit = VisitRecord(
            pet_id=data['pet_id'],
            date=data['date'],
            symptoms=data['symptoms'],
            treatment=data['treatment'],
            next_visit=data.get('next_visit', '')
        )
        db.session.add(visit)
        db.session.commit()
        return jsonify({'message': 'Visit recorded'}), 201

    visits = VisitRecord.query.all()
    return jsonify([
        {
            'id': v.id,
            'pet_id': v.pet_id,
            'pet_name': v.pet.name,
            'date': v.date,
            'symptoms': v.symptoms,
            'treatment': v.treatment,
            'next_visit': v.next_visit
        }
        for v in visits
    ])


# ----------------------------
# Run the app
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
