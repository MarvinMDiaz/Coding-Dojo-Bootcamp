from flask import render_template,request,redirect,session
from flask_app import app
from flask import flash
from flask_app.models.user import User
from flask_app.models.tree import Tree

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def root():

    return redirect('/home')

@app.route('/home')
def home():

    return render_template('sign_in_up.html')

@app.route('/home/sign_up')
def sign_up():

    return render_template("sign_up.html")


@app.route('/home/new_user', methods=["POST"])
def new_user():
    if not User.validate_form(request.form):
        print("working")
        return redirect('/home/sign_up')
    print("still Working")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }
    
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name']= request.form['first_name']

    return redirect('/home')


@app.route('/home/login',methods=["POST"])
def login():

    if not User.validate_login(request.form):
        return redirect('/')

    data = {"email" : request.form["email"]}
    
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/home")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/home')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name


    return redirect("/dashboard")



@app.route('/dashboard')
def dash():
    if not 'user_id' in session: 
        flash('log in')
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    user= User.get_one(data)
    trees = Tree.trees_users()
    return render_template('dash.html',user= user, trees= trees)

@app.route('/sign_out')
def log_off():
    session.clear()

    return redirect('/')





