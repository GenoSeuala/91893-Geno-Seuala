from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import random  # Import the random module

# Create a Flask app instance
app = Flask(__name__)

# Set a secret key for flash messages (used to show alerts to the user)
app.secret_key = "supersecretkey"


def get_db_connection():
    # Connect to 'EzChef.db' database
    conn = sqlite3.connect('EzChef.db')
    # This makes it easier to access rows as dictionaries
    conn.row_factory = sqlite3.Row
    return conn

# Route for the home page ('/')

@app.route('/')
def index():
    return render_template('base.html')
