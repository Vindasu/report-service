"""
Statistics Microservice
Port: 5003
"""

from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)


@app.route('/average', methods=['POST'])
def calculate_average():
    """
    Calculate average.
    """
    try:
        data = request.get_json()

        # Verify that input is an array
        if not isinstance(data, list):
            return jsonify({"ERROR": "Invalid input format. Expected an array."}), 400

        average = sum(data) / len(data)
        return jsonify({"average": average}), 200

    except Exception as e:
        return jsonify({"ERROR": str(e)}), 400


@app.route('/sum', methods=['POST'])
def calculate_sum():
    pass


@app.route('/minimum', methods=['POST'])
def calculate_minimum():
    pass


if __name__ == '__main__':
    print("\n" + "="*50)
    print("📊 Statistics Microservice Running")
    print("🌐 http://localhost:5003")
    print("="*50 + "\n")

    app.run(host='localhost', port=5003, debug=True)