from flask import Blueprint, render_template, url_for, request, redirect,json
from .models import Userevent
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return render_template("index.html")

@auth.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':

        user =  request.form['textname'];
        Phonenumber= request.form['number'];
        # print("stroe data base")
        emailid=request.form['email'];
        fa=request.form['fa'];
        new_user=Userevent(name=user,email=emailid,gender=fa,phone=Phonenumber)
        db.session.add(new_user)
        db.session.commit()
    return json.dumps({'status':'OK','user':user,'Phonenumber':Phonenumber,'emailid':emailid,'fa':fa});
@auth.route('/view')
def view():
    return render_template('view.html',Userevent = Userevent.query.all())
@auth.route('/<id>/editfrom',methods=['GET','POST'])
def editfrom(id):
    print("id value")
    print(id)
    
    return render_template("editfrom.html",Userevent =Userevent.query.get(id))
@auth.route('/<id>/delfrom',methods=['GET','POST'])
def delfrom(id):
    user=Userevent.query.get(id)
    db.session.delete(user)
    db.session.commit()
    
    return render_template('view.html')