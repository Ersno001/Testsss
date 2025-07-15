from flask import Flask
from flask_cors import CORS
from models import db
from routes.auth import auth_bp
from routes.movies import movies_bp
from routes.payment import payment_bp
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET')

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(movies_bp, url_prefix="/movies")
app.register_blueprint(payment_bp, url_prefix="/payment")

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
