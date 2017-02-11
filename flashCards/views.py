from flask import Flask, render_template, g, jsonify, redirect
from data import Card
from flashCards import app
# import sqlite3

#app = Flask(__name__)
#app.debug = True

# @app.before_request
# def before_request():
#     g.db = sqlite3.connect("cards.db")
# 
# @app.teardown_request
# def teardown_request(exception):
#     if hasattr(g, 'db'):
#         g.db.close()
# 
# @app.route('/add')
# def signup():
#     card = "annieemail"
#     g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
#     g.db.commit()
#     return redirect('/')
# @app.route('/get')
# def emails():
#     email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
#     return jsonify(email_addresses)

def getCardArr():
    card0 = Card(0, "stefano-veneziano.jpg","artist", "Madonna and Child Enthroned", "1369", "Museo Correr, Venice", "idk")
    card1 = Card(1, "doges.jpg", "idk", "Doges Palace", "Begun 1340", "Venice", "building")
    return [card0, card1]

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return render_template('layout.html')
@app.route('/hello/child')
def child():
    return render_template('child.html')


@app.route('/cards/<_id>')
def cards(_id):
  #  return render_template('card.html', card=cards[_id])
    cards = getCardArr()
    print("NAME: ".format(cards[0].name)) 
    return render_template('card.html', card=cards[int(_id)])
