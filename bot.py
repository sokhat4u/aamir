from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data
links = {
    "trendence-survey.com": "https://s.cint.com/Survey/Complete",
    "example-survey.com": "https://example.com/survey/complete"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-link", methods=["POST"])
def get_link():
    data = request.get_json()
    host_name = data.get("host_name")
    completed_link = links.get(host_name, "Completed link not found")
    return jsonify({"completed_link": completed_link})

@app.route("/get-hostnames", methods=["GET"])
def get_hostnames():
    return jsonify({"hostnames": list(links.keys())})

if __name__ == "__main__":
    # Start Flask app without ngrok
    app.run(host="0.0.0.0", port=5000, debug=True)