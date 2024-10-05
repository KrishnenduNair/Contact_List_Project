## CRUD: Create Read Update Delete

## create ko kya pass karna hai?
# - first name
# - last name
#  - email

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])    #decorator
def get_contacts():
    contacts = Contact.query.all() ## gets the ORM to get all the contacts that exist in the database
    json_contacts = list(map(lambda x: x.to_json(), contacts)) ##map takes a list applies a func to it and returns a new list & map func gives map obj toh llist me convert karne ke liye list()
    return jsonify({"contacts": json_contacts})

@app.route("/create_contacts", methods=["POST"])
def create_contacts():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Invalid JSON payload"}), 400

        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")

        if not first_name or not last_name or not email:
            return jsonify({"message": "You must include a first name, last name and email"}), 400

        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "User  created!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500
        
    return jsonify({"message": "User created!"}), 201

@app.route("/update_contacts/<int:user_id>", methods=["PATCH"])
def update_contacts(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    db.session.commit()
    
    return jsonify({"message": "User updated!"}), 200

@app.route("/delete_contacts/<int:user_id>", methods=["DELETE"])
def delete_contacts(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200    
        
if __name__ == "__main__":
    with app.app_context():#creates all the models if not created already
        db.create_all()
        
    app.run(debug=True)
