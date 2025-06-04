from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/tool", methods=["POST"])
def tool():
    data = request.json
    query = data.get("query", "")
    return jsonify({"result": f"Tool executed successfully for query: {query}"})

if __name__ == "__main__":
    app.run(port=5001)