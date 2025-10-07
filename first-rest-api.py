import mysql.connector
from flask import Flask, jsonify, send_from_directory
from flask import Flask
from flask_cors import CORS
import os

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

app = Flask(__name__)
CORS(app)  # <--- abilita CORS per tutte le route

@app.route("/Hello")
def hello():
    return "Hello, World!"

@app.route("/")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    
    # Prendi i nomi delle colonne
    column_names = [desc[0] for desc in mycursor.description]
    
    # Converti i risultati in lista di dizionari e aggiungi image_url
    result = []
    for row in myresult:
        unit_dict = dict(zip(column_names, row))
        unit_name = unit_dict.get('Unit', '').replace(' ', '%20')
        unit_dict['image_url'] = f"assets/clash_royale_sprites/{unit_name}.png"
        result.append(unit_dict)
    
    # Usa jsonify per restituire un JSON corretto
    return jsonify(result)

@app.route('/air_troop')
def airTransport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE transport = 'Air'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return str(result)  # ritorno la lista come stringa

@app.route('/epic_units')
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'epic'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return str(result)

@app.route('/common_units')
def commonUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'common'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return str(result)

@app.route('/unit_count')
def unitCount():
    mycursor.execute("SELECT COUNT(*) FROM CLASH_ROYALE.Clash_Unit")
    count = mycursor.fetchone()[0]
    print(count)
    return str(count)


@app.route('/images')
def list_images():
    images = []
    for root, dirs, files in os.walk(ASSETS_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                rel_dir = os.path.relpath(root, ASSETS_DIR)
                rel_file = os.path.join(rel_dir, file) if rel_dir != '.' else file
                images.append(f"/assets/{rel_file}")
    return jsonify(images)

@app.route('/assets/<path:filename>')
def serve_image(filename):
    return send_from_directory(ASSETS_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)