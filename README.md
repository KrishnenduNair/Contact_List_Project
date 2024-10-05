# Contact List Project

# Overview
This full stack project is a simple contact list application built using Python and Flask. It allows users to create, read , update, and delete contacts basically implementing CRUD operations.

# Features
Create new contacts<br>
View all contacts<br>
Update existing contacts<br>
Delete contacts<br>

# Requirements
Python 3.6 or higher
Flask 2.0 or higher
SQLite database

# Usage
Open a web browser and navigate to http://localhost:5000
Click on the "Create Contact" button to create a new contact
Fill in the contact information and click "Submit"
Update or delete contacts by clicking on the "Update" or "Delete" buttons

# API Endpoints
GET /contacts: Retrieve all contacts
POST /create_contacts: Create a new contact
PATCH /update_contacts/<id>: Update a contact
DELETE /delete_contacts/<id>: Delete a contact

# Database Schema
The database schema is defined in the models.py file. It consists of a single table called "contacts" with the following columns:

id: Unique identifier for the contact
name: Name of the contact
email: Email address of the contact
phone: Phone number of the contact
