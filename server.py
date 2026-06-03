from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/api/message", methods=["POST"])
def message():
    data = request.json
    messages.append(data)

    print("NEW MESSAGE:", data)

    return jsonify({"status": "saved"})

@app.route("/api/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

app.run(host="0.0.0.0", port=5000)