
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    requirement = db.Column(db.Text)
    status = db.Column(db.String(20), default="Pending")

# Routes

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    contact = Contact(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        message=data.get('message')
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({"message": "Contact saved"}), 201


@app.route('/inquiry', methods=['POST'])
def inquiry():
    data = request.json
    inquiry = Inquiry(
        service=data.get('service'),
        requirement=data.get('requirement')
    )
    db.session.add(inquiry)
    db.session.commit()
    return jsonify({"message": "Inquiry submitted"}), 201


@app.route('/admin/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "email": c.email,
        "phone": c.phone,
        "message": c.message
    } for c in contacts])


@app.route('/admin/inquiries', methods=['GET'])
def get_inquiries():
    inquiries = Inquiry.query.all()
    return jsonify([{
        "id": i.id,
        "service": i.service,
        "requirement": i.requirement,
        "status": i.status
    } for i in inquiries])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
