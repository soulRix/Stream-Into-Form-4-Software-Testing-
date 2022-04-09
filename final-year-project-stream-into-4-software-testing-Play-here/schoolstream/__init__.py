import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_user import  roles_required, UserManager, UserMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, login_required
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail


app = Flask(__name__)


#Flask Config
app.config['SECRET_KEY'] = '39ddb37d7e4aff869b861de048d7c08cd1fa2acf5a2bd7dff0acc127f771893c'

#Flask SQLALCHEMY Config
#Old Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schoolstream.db'

#New Database MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/school_stream_testing' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Avoid SQLAlchemy warning

#Flask Mail Config
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

# Debuger Tool  Config
#app.config['DEBUG_TB_PROFILER_ENABLED'] = True
#app.debug = True




#==================================================#
#Extension
db = SQLAlchemy(app) #SQL instance
bcrypt = Bcrypt(app) #Initialize the Bcrypt 
login_manager = LoginManager(app)
login_manager.login_view = 'loginPage'
login_manager.login_message_category = 'info'
mail = Mail(app)


# Debuger Tool
#toolbar = DebugToolbarExtension(app)

#==================================================#

from schoolstream import routes