from flask import Flask, jsonify
from repository.database import db
import os 
from db_models.payment import Payment

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
  return jsonify({'message': 'Pix payment created'})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
  return jsonify({'message': 'Pix payment confirmed'})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
  return 'Pagamento pix.'

if __name__ == '__main__':
  app.run(debug=True)