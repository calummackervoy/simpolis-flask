import json
from flask import Flask, request, jsonify
from rdflib import Graph
from urllib.parse import unquote_plus
from pymongo import MongoClient
from bson import json_util

# config

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.simpolis

@app.route("/")
def main():
    return None, 204

@app.route("/world/", methods=['POST', 'GET'])
def world():
    if request.method == 'POST':
        g = Graph().parse(data=json.dumps(request.get_json()), format='json-ld')
        jsonld = json.loads(g.serialize(format='json-ld'))
        
        return jsonify(jsonld), 200, {'Content-Type': 'application/ld+json'}

        '''jsonld = request.get_json()

        # assign the graph an id
        if "@id" not in jsonld:
            jsonld["@id"] = "http://localhost:5000/world/"

        # creates or updates the world graph
        db.world.find_one_and_replace(
            {"@id": jsonld["@id"]},
            jsonld,
            upsert=True
        )
        return jsonify(jsonld), 200'''

    g = Graph().parse(data=json_util.dumps(db.world.find_one()), format='json-ld')
    jsonld = json.loads(g.serialize(format='json-ld'))
    return jsonify(jsonld), 200, {'Content-Type': 'application/ld+json'}
    #return jsonify(json.loads(json_util.dumps(db.world.find_one()))), 200, {'Content-Type': 'application/ld+json'}
