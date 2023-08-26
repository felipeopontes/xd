from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')

def home():
    return 'Minha primeira API'

@app.route('/sentimento/<frase>')

def sentimento(frase):
    tb= TextBlob(frase)
    polaridade = tb.sentiment.polarity
    return str(polaridade)


app.run(debug=True)