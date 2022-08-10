from flask import render_template,request,redirect,session
from flask_app import app
from flask import flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



@app.route('/')
def home():

    return render_template('reg.html')

@app.route('/new_user', methods=["POST"])
def registration():
    
    if not User.validate_form(request.form):
        print("working")
        return redirect('/')
    print("still Working")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }
    
    # ... do other things
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name']= request.form['first_name']

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():

    return render_template('dash.html')

@app.route('/login', methods=["POST"])
def login(): 

    if not User.validate_login(request.form):
        # we redirect to the template with the form.
        return redirect('/')

    data = {"email" : request.form["email"]}
    
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    # never render on a post!!!
    return redirect("/dashboard")

@app.route('/sign_out')
def log_off():
    session.clear()

    return redirect('/')



@app.route('/reg')
def loginreg():
    

    return render_template('chall.html')