import flask
from flask import request, jsonify
from app.ntuc import search as searchNTUC

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/ntuc/', methods=['POST'])
def queryNTUC():
    return searchNTUC(request.get_json()['query'])
