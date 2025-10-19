import mysql.connector # Importa il modulo necessario per connettersi e interagire con un database MySQL
from flask import Flask, jsonify, send_from_directory  # Importa le classi e funzioni principali da Flask:
from flask import Flask
from flask_cors import CORS # Importa l'estensione CORS (Cross-Origin Resource Sharing), che permette al server di accettare richieste da domini diversi
import os  # Importa il modulo 'os' per interagire con il sistema operativo

#Connect to mysql
mydb = mysql.connector.connect(  # Stabilisce la connessione al database MySQL
  host="localhost", # Specifica l'indirizzo del server del database
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()  # Crea un oggetto cursore, che è lo strumento utilizzato per eseguire le query SQL

# Definisce il percorso assoluto della directory 'assets' unendolo alla directory in cui si trova lo script corrente
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')  

app = Flask(__name__) # Crea la richiesta dell'applicazione Flask
CORS(app)  # <--- abilita CORS per tutte le route

@app.route("/Hello")
def hello():
    return "Hello, World!"

@app.route("/")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")  # Esegue la query SQL per selezionare tutti i dati dalla tabella Clash_Unit
    myresult = mycursor.fetchall()  # Recupera tutti i risultati della query eseguita
     
    # Prendi i nomi delle colonne
    column_names = [desc[0] for desc in mycursor.description] # Ottiene i nomi delle colonne dalla descrizione del cursore
    
    # Converti i risultati in lista di dizionari e aggiungi image_url
    result = [] # Inizializza una lista vuota per memorizzare i risultati
    for row in myresult:  # Ripete su ogni riga dei risultati ottenuti
        unit_dict = dict(zip(column_names, row)) # Crea un dizionario per ogni riga, associando i nomi delle colonne ai valori corrispondenti
        unit_name = unit_dict.get('Unit', '').replace(' ', '%20') # Sostituisce gli spazi nel nome dell'unità con '%20' per l'URL
        unit_dict['image_url'] = f"assets/clash_royale_sprites/{unit_name}.png" # Aggiunge un campo 'image_url' al dizionario con il percorso dell'immagine
        result.append(unit_dict) # Aggiunge il dizionario alla lista dei risultati
    
    # Usa jsonify per restituire un JSON corretto
    return jsonify(result)

@app.route('/air_troop') # Definisce una route per ottenere tutte le unità di trasporto aereo
def airTransport(): 
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE transport = 'Air'") # Esegue la query SQL per selezionare tutte le unità con trasporto aereo
    myresult = mycursor.fetchall() # Recupera tutti i risultati della query eseguita
    result = [] # Inizializza una lista vuota per memorizzare i risultati
    for x in myresult: # Ripete su ogni risultato ottenuto
        print(x)
        result.append(x) # Aggiunge ogni risultato alla lista
    return str(result)  # ritorno la lista come stringa

@app.route('/epic_units') # Definisce una route per ottenere tutte le unità epiche
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'epic'") # Esegue la query SQL per selezionare tutte le unità con rarità epica
    myresult = mycursor.fetchall() 
    result = []  
    for x in myresult: 
        print(x)
        result.append(x)
    return str(result)

@app.route('/common_units') # Definisce una route per ottenere tutte le unità comuni
def commonUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'common'") # Esegue la query SQL per selezionare tutte le unità con rarità comune
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return str(result)

@app.route('/unit_count') # Definisce una route per ottenere il conteggio totale delle unità
def unitCount():
    mycursor.execute("SELECT COUNT(*) FROM CLASH_ROYALE.Clash_Unit") # Esegue la query SQL per contare il numero totale di unità nella tabella Clash_Unit
    count = mycursor.fetchone()[0] # Recupera il conteggio dalla query eseguita
    print(count)
    return str(count)


@app.route('/images') # Definisce una route per elencare tutte le immagini nella directory 'assets'
def list_images():
    images = [] 
    for root, dirs, files in os.walk(ASSETS_DIR): # Cammina attraverso la directory 'assets' e le sue sottodirectory
        for file in files: # Per ogni file trovato
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')): # Controlla se il file è un'immagine basata sull'estensione
                rel_dir = os.path.relpath(root, ASSETS_DIR) # Ottiene il percorso relativo della directory corrente rispetto a 'assets'
                rel_file = os.path.join(rel_dir, file) if rel_dir != '.' else file # Costruisce il percorso relativo del file
                images.append(f"/assets/{rel_file}") # Aggiunge il percorso dell'immagine alla lista
    return jsonify(images) # Restituisce la lista delle immagini come JSON

@app.route('/assets/<path:filename>') # Definisce una route per servire le immagini dalla directory 'assets'
def serve_image(filename):
    return send_from_directory(ASSETS_DIR, filename) # Invia il file richiesto dalla directory 'assets'

if __name__ == "__main__": # Avvia l'applicazione Flask in modalità di debug
    app.run(debug=True) 