import json
from flask import Flask, request, jsonify
from rdflib import Graph
from urllib.parse import unquote_plus

app = Flask(__name__)

@app.route("/")
def main():
    return None, 204

@app.route("/world/", methods=['POST', 'GET'])
def world():
    if request.method == 'POST':
        g = Graph().parse(data=json.dumps(request.get_json()), format='json-ld')
        
        return jsonify(g.serialize(format='json-ld')), 200

    data = {
        "@context": {
            "hasTileMap": {
                "@id": "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mudworld.ttl#hasTileMap",
                "@container": "@list"
            }
        },
        "@id": "http://example.org/people#joebob",
        "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mudworld.ttl#Region": {
            "http://xmlns.com/foaf/0.1/name": "Attica",
            "hasTileMap": [
                [0,0,0],
                [0,0,0]
            ]
        }
    }

    return jsonify(data), 200, {'Content-Type': 'application/ld+json'}
