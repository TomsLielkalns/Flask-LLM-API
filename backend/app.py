from flask import Flask, request, jsonify

from helpers.send_req_to_api import send_to_hf

app = Flask(__name__)


@app.route("/summerize", methods=["POST"])
def summerize():
    data = request.get_json(silent=True)
    input_text = data.get("input_text")

    if not input_text:
        return jsonify({"error": "No input text provided"}), 400
    
    try:
        return jsonify(send_to_hf(f'Summarize the following text:\n "{input_text}"'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)