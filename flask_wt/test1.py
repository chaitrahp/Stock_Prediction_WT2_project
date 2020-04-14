from flask import Flask, render_template , request
from flask_bootstrap import StaticCDN
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index1.html")
    #requests.get("templates/index.html")


#Login with
@app.route('/facebook',methods=['GET'])
def facebook():
    requests.get("https://www.facebook.com")

@app.route('/twitter',methods=['GET'])
def twitter():
    requests.get("https://twitter.com/login?lang=en")

@app.route('/google',methods=['GET'])
def google():
    requests.get("https://accounts.google.com/AccountChooser?service=lso")

@app.route('/instagram',methods=['GET'])
def instagram():
    requests.get("https://www.instagram.com/accounts/login/")
#Google font
@app.route('/googlefonts',methods=['GET'])
def googlefonts():
    requests.get("https://fonts.googleapis.com/css?family=Open+Sans:300,400,400i,600,700|Raleway:300,400,400i,500,500i,700,800,900")
