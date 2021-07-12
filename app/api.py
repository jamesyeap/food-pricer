import flask
from flask import request, jsonify
from app.ntuc import search as searchNTUC
from app.cold_storage import search as searchColdStorage

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def queryAll():
    resultsColdStorage = searchColdStorage(request.get_json()['query']) 
    resultsNTUC = searchNTUC(request.get_json()['query'])

    resultsCombined = resultsColdStorage + resultsNTUC

    return jsonify({"results": resultsCombined})

@app.route('/ntuc/', methods=['POST'])
def queryNTUC():
    return jsonify({"results": searchNTUC(request.get_json()['query'])})

@app.route('/cold-storage/', methods=['POST'])
def queryColdStorage():
    return jsonify({"results": searchColdStorage(request.get_json()['query'])})
