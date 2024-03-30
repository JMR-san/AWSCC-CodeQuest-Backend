from flask import Flask, render_template, request, redirect, url_for
import string
import secrets

app = Flask(__name__)

passwords = []

@app.route('/')
def index():
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['POST'])
def add_password():
    website = request.form['website']
    email = request.form['email']
    password = generate_password()
    passwords.append({'website': website, 'email': email, 'password': password})
    return redirect(url_for('index'))

@app.route('/update_password/<int:index>', methods=['POST'])
def update_password(index):
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    passwords[index] = {'website': website, 'email': email, 'password': password}
    return redirect(url_for('index'))

@app.route('/delete_password/<int:index>')
def delete_password(index):
    del passwords[index]
    return redirect(url_for('index'))

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
