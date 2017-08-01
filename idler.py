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
    session['gold'] = 0
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

@app.route('/action',methods=['POST'])
def action():
    if session['enemy']:
        ERROR.error = 'currently fighting an enemy'
        return jsonify(ERROR)
    else:
        session['enemy'] = new Mob(session['Character'].level)
        # we could either return html here or json and generate the html client side
        return enemy_encountered()

@app.route('/fight',methods=['POST'])
def fight():
    results = fight(session['character'],session['enemy'])
    if results.status == 'completed':
        # loot should generate gold based on character level, and the active resources 
        session['gold'] += loot(session['character'].level,session['resources'])
        if resource_found():
            session['resource'].append(Resource())

    return jsonify(results)

@app.route()

@app.route('')
if __name__ == '__main__':
    app.run()

