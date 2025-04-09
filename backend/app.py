from flask import Flask, request, jsonify, abort

from helpers.send_req_to_api import send_to_hf
from helpers.parse_file import parse_file

app = Flask(__name__)


@app.route("/summerize", methods=["POST"])
def summerize():
    text = request.get_data(as_text=True)
    file = request.files.get("file")

    if file:
        text = parse_file(file, abort)

    if not text:
        return jsonify({"error": "No input text or file provided"}), 400
    
    try:
        return jsonify(send_to_hf(f'Summarize the following text:\n "{text}"'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)