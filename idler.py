from flask import Flask, request, jsonify, session
from model.character import Character
from messages import SUCCESS,ERROR

app = Flask(__name__)
app.secret_key = "Secret Szechuan Sauce"


@app.route('/')
def index():
# way #1 to do things

@app.route('/login',methods=['POST'])
def login():
    json = request.get_json()
    session['username'] = json['username']
    session['character'] = Character()
    session['resources'] = Resources()
    return jsonify(SUCCESS)

@app.route('/logout', methods=['POST'])
def logout():
    if 'username' in session:
        session.pop('username')
        session.pop('character')
        return jsonify(SUCCESS)
    else:
        ERROR.error = 'not logged in'
        return jsonify(ERROR)

if __name__ == '__main__':
    app.run()

