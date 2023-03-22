import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route("/")
def startseite():

    return render_template("index.html")

@app.route("/Mathematik")
def mathematik():

    return render_template("Mathe.html")


if __name__ == '__main__':  
    app.run(debug=True)

#datenbank Befehle
#connection = sqlite3.connect('user.db')
#connection.execute()
#connection.commit()
#connection.close()