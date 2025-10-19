# save this as app.py
import mysql.connector # Per connettersi a un database MySQL
import pandas as pd  # Importa la libreria Pandas, per leggere i dati dal file CSV
from flask import Flask # Importa Flask per creare l'applicazione web
from flask_cors import CORS 

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)
mycursor = mydb.cursor() # Crea un oggetto cursore per eseguire comandi SQL

app = Flask(__name__) # Crea la richiesta dell'applicazione Flask
CORS(app)  # <--- abilita CORS per tutte le route



mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASH_ROYALE") # Crea il database CLASH_ROYALE se non esiste già

# Crea la tabella Clash_Unit con le specifiche delle unità di Clash Royale
mycursor.execute(""" 
  CREATE TABLE IF NOT EXISTS CLASH_ROYALE.Clash_Unit (  
    Unit VARCHAR(30) NOT NULL,
    Cost INTEGER,
    Hit_Speed VARCHAR(30),
    Speed VARCHAR(30),
    Deploy_Time VARCHAR(30),
    Range_ VARCHAR(30),
    Target VARCHAR(30),
    Count VARCHAR(30),
    Transport VARCHAR(30),
    Type VARCHAR(30),
    Rarity VARCHAR(30),
    PRIMARY KEY (Unit)
  );""")   


mycursor.execute("DELETE FROM CLASH_ROYALE.Clash_Unit") # Pulisce la tabella prima di inserire nuovi dati
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',') # Legge i dati dal file CSV in un DataFrame di Pandas
clash_data = clash_data.fillna('Null') # Sostituisce i valori NaN con la stringa 'Null'
# Aggiungi la colonna ImageUrl con il link all'immagine, sostituendo gli spazi con %20
clash_data['ImageUrl'] = clash_data['Unit'].apply(lambda name: f"assets/clash_royale_sprites/{name.replace(' ', '%20')}.png") 
print(clash_data.head(20)) # Stampa le prime 20 righe del DataFrame per verifica

#Fill the table
for i,row in clash_data.iterrows(): 
    cursor = mydb.cursor() # Create a cursor object
    #here %S means string values  
    sql = "INSERT INTO CLASH_ROYALE.Clash_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # Create insert query
    cursor.execute(sql, tuple(row))  # Execute the query with the row data
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit() # Commit the transaction

#Check if the table has been filled
mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit") # Esegue la query SQL per selezionare tutti i dati dalla tabella Clash_Unit
myresult = mycursor.fetchall() # Recupera tutti i risultati della query eseguita

for x in myresult:
  print(x) # Stampa ogni riga dei risultati ottenuti