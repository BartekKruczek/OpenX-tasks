import random

from flask import Flask, jsonify, request
from utils import Utils

app = Flask(__name__)
app_id_random = random.randint(0, 1000)

@app.route('/calculate_celsius', methods=['POST'])
def main() -> None:
    data = request.json

    # checking if the request is empty
    if not data:
        return jsonify({"message": "Request is empty"}), 400
    
    # checking if the request has the key 'farenheit'
    if 'farenheit' not in data:
        return jsonify({"message": "Request does not have the key 'farenheit'"}), 400
    
    # returning the converted temperature
    return jsonify({"message": Utils(data['farenheit']).temperature_converter_to_Celsius()})

if __name__ == '__main__':
    app.run(debug=True)