from flask import Flask, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # default MongoDB port
db = client['CareerMatch']  # Create/use a database
collection = db['Jobs']  # Create/use a collection

@app.route('/add_job', methods=['POST'])
def add_text():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']
    # Insert into MongoDB
    result = collection.insert_one({"text": text})

    return jsonify({"message": "Text added successfully!", "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
