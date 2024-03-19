from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    name = request.form['name']
    record_to_mongodb(name)
    return f"Hello, {name}! Your name has been recorded."

def record_to_mongodb(name):
    record = {"name": name}
    collection.insert_one(record)

if __name__ == '__main__':
    app.run(debug=True)
