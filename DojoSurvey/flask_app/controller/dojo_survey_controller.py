from flask import render_template,request,redirect,session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print('Got Post from Survey')
    print(request.form)
    # print(request.form['location'])
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']

    data= {
        
        "name": request.form["name"],
        "location": request.form["location"],
        "comment": request.form["comment"],
        "language": request.form["language"],
    }

    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Dojo.save(request.form)
    Dojo.save(data)
    
    return redirect('/result')


@app.route('/result')
def show_user():
    return render_template('result.html')
