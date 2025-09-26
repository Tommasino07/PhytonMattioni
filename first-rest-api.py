import mysql.connector
from flask import Flask

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route('/air_transport')
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