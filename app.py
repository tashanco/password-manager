from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password_manager.db'
db = SQLAlchemy(app)

## Database Models
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Password %r>' % self.id

## Index Page Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        new_password = Password(username=username, password=password)
        try:
            db.session.add(new_password)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue with adding your password'   
    else:
        passwords = Password.query.order_by(Password.id).all()
        return render_template('index.html', passwords=passwords)

## Delete Route
@app.route('/delete/int:id', methods=['GET', 'POST'])
def delete(id):
    password_to_delete = Password.query.get_or_404(id)

    try:
        db.session.delete(password_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your password'

## Update Route
@app.route('/update/int:id', methods=['GET', 'POST'])
def update(id):
    password = Password.query.get_or_404(id)
    if request.method == 'POST':
        password_to_update = Password.query.get_or_404(id)

        password_to_update.username = request.form['name']
        password_to_update.password = request.form['password']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your password'
    else:
        return render_template('update.html', password=password)
        
if __name__ == '__main__':
    app.run(debug=True)