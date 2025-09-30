from flask import Flask, send_file, jsonify
import json
import random

app = Flask(__name__)

@app.route("/nba")
def books():
    return send_file('nba.json')

@app.route("/rnd")
def rnd():
    with open('nba.json') as f:
        data = json.load(f)
    return jsonify(data['players'][random.randrange(0, len(data['players']))])

# Nuova rotta per ricevere un parametro: id del giocatore
@app.route("/player/<int:player_id>")
def get_player(player_id):
    with open('nba.json') as f:
        data = json.load(f)
    player = None
    for p in data['players']:
        if p['id'] == player_id:
            player = p
            break  # Esce dal ciclo appena trova il giocatore
    if player:
        return jsonify(player)
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == "__main__":
    app.run()


    
