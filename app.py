from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.app_context().push()

class test(db.Model):
    Invoice=db.Column(db.Integer, primary_key=True)
    Date_d=db.Column(db.DateTime, default=datetime.utcnow)
    Party_name=db.Column(db.String(200),nullable=False)
    Taxable_value=db.Column(db.String(200),nullable=False)
    Gst_number=db.Column(db.Float)
    Cgst=db.Column(db.Float)
    Sgst=db.Column(db.Float)
    Igst=db.Column(db.Float)
    Gst_value=db.Column(db.Float)
    Invoice_value=db.Column(db.Float)

def __repr__(self):
    return 'test %r' % self.Party_name
   


@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/sales')
def sales():
    Test =test(Party_name="purna",Taxable_value=100,Gst_number=100,Cgst=100,Sgst=100,Igst=100,Gst_value=100,Invoice_value=100)
    db.session.add(Test)
    db.session.commit()
    alltest=test.query.all()
    return render_template("sales.html",alltest=alltest)


@app.route('/Purchase')
def Purchase():
    alltest=test.query.all()
    print(alltest)
    return render_template("Purchase.html")

@app.route('/Taxable')
def Tax():
    return render_template("Taxable.html")

if __name__=="__main__": 
    app.debug=True   
    app.run()
    