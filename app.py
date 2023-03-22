import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route("/")

@app.route("/index", methods=['POST'])

connection.execute()
connection.commit()
connection.close()