from flask import Blueprint, render_template


misc = Blueprint('misc', __name__)

@misc.route("/")
def splash(name=None):
	return render_template('index.html')

@misc.route("/wordcheat")
def cheat(name=None):
	f = open("web_sandbox/static/ospd.txt")
	return render_template('wordCheat.html', wordlist = f.read().splitlines())
