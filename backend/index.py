from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask and PostgreSQL!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
