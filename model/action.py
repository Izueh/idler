from flask.views import MethodView
from flask import request, jsonify

class Attack(MethodView):
    def post(self):
        json = request.get_json()
        # handle request
        # make response
        return jsonify(response) 

