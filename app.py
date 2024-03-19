
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Replace the following variables with your own values
MONGO_URI = "mongodb+srv://sakethvudala:<password>@cluster7.egvf438.mongodb.net/?retryWrites=true&w=majority&appName=Cluster7"
DB_NAME = "chat_records"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

@app.route("/api/todos", methods=["GET", "POST"])
def handle_todos():
    if request.method == "GET":
        # Return a list of todos
        records = list(db.chat_records.find())
        return jsonify(records)
    elif request.method == "POST":
        # Add a new todo
        data = request.get_json()
        db.chat_records.insert_one({"query_text": data["query_text"], "response_text": data["response_text"], "intent": data["intent"]})
        return jsonify({"message": "Todo added successfully"})

if __name__ == "__main__":
    app.run(debug=True)