"""
Statistics Microservice
Port: 5003
"""

from flask import Flask, request, jsonify, abort

# Create a Flask app
app = Flask(__name__)

# ---------------------------- Helper

def require_json_list():
    """
        Validates that request JSON body exists and is a non-empty list of numbers.
        if fail, aborts with 400 and descriptive message
        returns: validated list of nums if success
    """
    # check that request is a json
    if not request.is_json:
        abort(400, description = "Content-Type must be application/json with a JSON body.")

    # make this silent so that Flask doesn't raise BadRequest exception
    # and raises our custom written error instead
    data = request.get_json(silent=True)

    if data is None:
        abort(400, description = "Invalid JSON body.")

    if not isinstance(data, list):
        abort(400, description = "Invalid input format. Expected a JSON array.")

    if len(data) == 0:
        abort(400, description = "Array must not be empty.")

    for i, val in enumerate(data):
        if not isinstance(val, (int, float)):
            abort(400, description = "All elements must be numbers.")
    return data

# ---------------------------- Error Handlers
# custom messages for possible errors
@app.errorhandler(400)
def handle_400(err):
    return jsonify({"error": "Bad Request", "message": err.description}), 400

@app.errorhandler(404)
def handle_404(err):
    return jsonify({"error": "Not Found", "message": "Endpoint does not exist."}), 404

@app.errorhandler(500)
def handle_500(err):
    return jsonify({"error": "Internal Server Error", "message": "Something went wrong."}), 500

# ---------------------------- Routes
# average, sum, and minimum
@app.route('/average', methods=['POST'])
def calculate_average():
    """
    Calculate average.
    """
    data = require_json_list()
    average = sum(data) / len(data)
    return jsonify({"average": average}), 200


@app.route('/sum', methods=['POST'])
def calculate_sum():
    """
    Calculate the sum of the given array of integers/floats.
    """
    data = require_json_list()
    return jsonify({"sum": sum(data)}), 200

@app.route('/minimum', methods=['POST'])
def calculate_minimum():
    """ Find the smallest value from the given array of integers/floats. """
    data = require_json_list()
    return jsonify({"minimum": min(data)}), 200


if __name__ == '__main__':
    print("\n" + "="*50)
    print("📊 Statistics Microservice Running")
    print("🌐 http://localhost:5003")
    print("="*50 + "\n")

    app.run(host='localhost', port=5003, debug=True) # TODO: remove debug when finalized
