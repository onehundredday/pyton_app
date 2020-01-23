from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/pythonDB'
else:
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://anhesdrarhxtak:8bd8798063a033daf37e59ceff36734157dab7a5e388e9bb7475db209ac995db@ec2-54-247-178-166.eu-west-1.compute.amazonaws.com:5432/d67mvg8v16v0it' 
   app.debug = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(200))
    choice = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    # def __init__(self, name, email, choice, rating, comments):
    #     self.name = name
    #     self.email = email
    #     self.choice = choice
    #     self.rating = rating
    #     self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        name  = request.form['name']
        email  = request.form['email']
        choice  = request.form['choice']
        rating  = request.form['rating']
        comments  = request.form['comments']
        #print(name, email, choice, rating, commets)
        if name == '' or choice == '':
            return render_template('index.html', message = 'Please enter required fields')
        #if db.session.query(Feedback).filter(Feedback.name == name).count == 0: # IT MEAN USER NOT IN DB
        data = Feedback(name, email, choice, rating, comments)
        db.session.add(data)
        db.session.commit()
        send_email(name, email, choice, rating, comments)
        return render_template('success.html')
if __name__ == '__main__':
  
    app.run()