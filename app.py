from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]

    if intent_name == "Intro.mynameis":
        name = req["queryResult"]["parameters"]["given-name"]
        record_to_mongodb(name)
        return jsonify({"fulfillmentText": f"Hello, {name}! Nice to meet you."})
    else:
        return jsonify({"fulfillmentText": "Intent not recognized"})

def record_to_mongodb(name):
    record = {"name": name}
    collection.insert_one(record)

if __name__ == '__main__':
    app.run(debug=True)
