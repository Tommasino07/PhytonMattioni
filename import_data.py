# save this as app.py
import mysql.connector
import pandas as pd
from flask import Flask
from flask_cors import CORS

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)  # <--- abilita CORS per tutte le route


#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASH_ROYALE")

#Create the table for the csv data (if not exists)
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

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM CLASH_ROYALE.Clash_Unit")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
# Aggiungi la colonna ImageUrl con il link all'immagine, sostituendo gli spazi con %20
clash_data['ImageUrl'] = clash_data['Unit'].apply(lambda name: f"assets/clash_royale_sprites/{name.replace(' ', '%20')}.png")
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO CLASH_ROYALE.Clash_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)