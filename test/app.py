from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
    host=mysql,
    user=root,
    password=password,
    database=secure_web_app
)
cursor = db.cursor()

# Endpoint to handle user registration
@app.route('register', methods=['POST'])
def register_user()
    # Get user input from request JSON
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate inputs (basic example)
    if not username or not password
        return jsonify({'error' 'Username and password are required.'}), 400

    # Securely insert user data using parameterized query
    try
        sql = INSERT INTO users (username, password) VALUES (%s, %s)
        cursor.execute(sql, (username, password))
        db.commit()
        return jsonify({'message' 'User registered successfully.'}), 201
    except Exception as e
        db.rollback()
        return jsonify({'error' str(e)}), 500

if __name__ == '__main__'
    app.run(host='0.0.0.0', port=80)
