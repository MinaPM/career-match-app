from flask import Flask, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # default MongoDB port
db = client['CareerMatch']  # Create/use a database
jobs_collection = db['Jobs']  # Create/use a collection
class_collection=db['Classes']
@app.route('/add_job', methods=['POST'])
def add_job():
    data = request.json
    if len(data)==0:
        return jsonify({"error": "No data provided"}), 400

    # Insert into MongoDB
    result = jobs_collection.insert_one(data)

    return jsonify({"message": "job added successfully!", "id": str(result.inserted_id)}), 201


@app.route('/add_class', methods=['POST'])
def add_class():
    data = request.json
    if len(data)==0:
        return jsonify({"error": "No data provided"}), 400

    # Insert into MongoDB
    result = class_collection.insert_one(data)

    return jsonify({"message": "classes added successfully!", "id": str(result.inserted_id)}), 201




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
