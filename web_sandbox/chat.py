from flask import Flask, render_template
from flask_socketio import SocketIO

# create and configure the chat app
capp = Flask(__name__, instance_relative_config=True, static_url_path='/static')
capp.config.from_pyfile('default_config.py')
capp.config.from_pyfile('config.py', silent=True)
socketio = SocketIO(capp)

@capp.route('/chat')
def sessions():
	return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
	print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('received my event: ' + str(json))
	socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
	socketio.run(capp, debug=True)
