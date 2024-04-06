from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import string
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['POST'])
def add_password():
    website = request.form['website']
    email = request.form['email']
    password = generate_password()
    new_password = Password(website=website, email=email, password=password)
    db.session.add(new_password)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_password/<int:id>', methods=['POST'])
def update_password(id):
    password = Password.query.get_or_404(id)
    password.website = request.form['website']
    password.email = request.form['email']
    password.password = request.form['password']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_password/<int:id>')
def delete_password(id):
    password = Password.query.get_or_404(id)
    db.session.delete(password)
    db.session.commit()
    return redirect(url_for('index'))

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)