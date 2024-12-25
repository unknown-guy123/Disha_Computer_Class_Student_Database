from flask import Flask, redirect, url_for, request, render_template
import psycopg2

app = Flask(__name__)

# Database configuration
DD_URL = 'postgresql://postgres:123456789@localhost:5432/manishafashion'

# Connect to the database
def connect():
    return psycopg2.connect(DD_URL)

if __name__ == '__main__':
    app.run(debug=True)