from flask import Flask
from flask import request

import control

app = Flask(__name__)

@app.route("/test")
def test_world():
    return "<p>Different String</p>"

@app.route("/player", methods=['POST'])
def create_player():
    # validation
    body = request.get_json()
    validity = control.player_creation_validity(body)

    if not validity:
        return 400
    
    msg, status = control.create_player(body)
    return msg, status

@app.route("/battle", methods=['POST'])
def battle_request():
    # validation
    body = request.get_json()
    validity = control.battle_validity(body)

    if not validity:
        return 400
    
    msg, status = control.battle_process(body)
    return msg, status

@app.errorhandler(404)
def page_not_found(e):
    return "The page you have requested cannot be found", 404

@app.errorhandler(500)
def page_not_found(e):
    return "Internal server error", 500

@app.route("/", methods=['GET'])
def health_check():
    return "Service is healthy", 200