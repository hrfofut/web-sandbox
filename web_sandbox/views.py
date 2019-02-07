from flask import Blueprint, render_template

misc = Blueprint('misc', __name__)

@misc.route("/")
def splash(name=None):
	return render_template('home.html')