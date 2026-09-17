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

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name: str):
    """ Delete a counter from COUNTERS """
    return jsonify({"Success": f"Counter {name}: {COUNTERS.pop(name)} deleted"}), status.HTTP_204_NO_CONTENT

@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Retrieve an existing counter"""
    return jsonify({name: COUNTERS[name]}), status.HTTP_200_OK

@app.route('/counters', methods=['GET'])
def list_counters():
    """List all counters"""
    return jsonify(COUNTERS), status.HTTP_200_OK
