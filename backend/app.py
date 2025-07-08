from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    cnic = db.Column(db.String(20))

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return "GreenPaws backend is running."

@app.route('/api/clients', methods=['GET', 'POST'])
def manage_clients():
    if request.method == 'POST':
        data = request.json
        client = Client(name=data['name'], phone=data['phone'], cnic=data.get('cnic'))
        db.session.add(client)
        db.session.commit()
        return jsonify({'message': 'Client added'}), 201

    clients = Client.query.all()
    return jsonify([{
        'id': c.id, 'name': c.name, 'phone': c.phone, 'cnic': c.cnic
    } for c in clients])

if __name__ == '__main__':
    app.run(debug=True)

