from flask import Flask, render_template
from flask_socketio import SocketIO
from xml.sax.saxutils import escape, unescape

# create and configure the chat app
capp = Flask(__name__, instance_relative_config=True, static_url_path='/static')
capp.config.from_pyfile('default_config.py')
capp.config.from_pyfile('config.py', silent=True)
socketio = SocketIO(capp)

html_escape_table = {
	'"': "&quot;",
	"'": "&apos;"
 }
html_unescape_table = {v:k for k, v in html_escape_table.items()}

@capp.route('/')
def sessions():
	return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
	print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('received my event: ' + str(json))
	if('message' in json.keys()):
		json['message'] = escape(json['message'], html_escape_table)
		json['user_name'] = escape(json['user_name'], html_escape_table)
	socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
	socketio.run(capp, debug=True)
