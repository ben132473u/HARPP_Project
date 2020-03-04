from flask import Flask
#from flask_mysqldb import MySQL
#from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
import dash
#import os


app = Flask(__name__)

#random key generated. can be useful for example session cookie, authentication etc.
#app.config['SECRET_KEY'] = os.urandom(24) 

#for graph
#dash_line_graph = dash.Dash(__name__, sharing=True, server = app, static_folder='static', url_base_pathname='/line/')
#dash_live_graph = dash.Dash(__name__, sharing=True, server = app, static_folder='static', url_base_pathname='/live/')



#SQL Config
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'xxx'
#app.config['MYSQL_DB'] = 'nextiot_flask_db'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


#init SQL
###mysql = MySQL(app)

#initializing logins, authentications and etc
#bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'


from mainFolder import routes
#import graph
#, line, live