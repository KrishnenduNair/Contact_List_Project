# Contact List Project

# Overview
This full stack project is a simple contact list application built using Python and Flask. It allows users to create, read , update, and delete contacts basically implementing CRUD operations.

# Features
Create new contacts<br>
View all contacts<br>
Update existing contacts<br>
Delete contacts<br>

# Requirements
Python 3.6 or higher<br>
Flask 2.0 or higher<br>
SQLite database<br>

# API Endpoints
GET /contacts: Retrieve all contacts<br>
POST /create_contacts: Create a new contact<br>
PATCH /update_contacts/<id>: Update a contact<br>
DELETE /delete_contacts/<id>: Delete a contact<br>

# Database Schema
The database schema is defined in the models.py file. It consists of a single table called "contacts" with the following columns:<br>
<br>
id: Unique identifier for the contact<br>
name: Name of the contact<br>
email: Email address of the contact<br>
phone: Phone number of the contact<br>
