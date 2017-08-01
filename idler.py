from flask import Flask, request, jsonify
from model.action import Attack

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"
# way #1 to do things
@app.route('/action/attack', methods=['POST'])
def attack():
    json = request.get_json()
    # handle request
    # make response
    return jsonify(response)

#way #2  more modular

app.add_url_rul('/action/attack2',view_func=Attack.as_view('attack',methods=['POST']))


    


if __name__ == '__main__':
    app.run()

