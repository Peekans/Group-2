"""
Counter API Implementation
"""
from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}

def counter_exists(name):
    """Check if counter exists"""
    return name in COUNTERS

def is_valid_counter_name(name):
    """Check whether a counter name is alphanumeric"""
    return name.isalnum()

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    if not is_valid_counter_name(name):
        return jsonify(
            {"error": f"Invalid counter name: {name}"}
        ), status.HTTP_400_BAD_REQUEST
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

@app.route('/counters', methods=['GET'])
def list_counters():
    """List all counters"""
    return jsonify(COUNTERS), status.HTTP_200_OK
