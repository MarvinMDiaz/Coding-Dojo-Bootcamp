from flask import render_template,request,redirect,session
from flask_app import app
from flask import flash
from flask_app.models.user import User
from flask_app.models.tree import Tree
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/dashboard/new_tree')
def new_tree():
    if not 'user_id' in session: 
        flash('log in')
        return redirect('/')

    return render_template('new_tree.html')

@app.route('/dashboard/new_tree/Create', methods=['POST'])
def create_tree():
    if not Tree.validate_tree(request.form):
        print("working")
        return redirect('/dashboard/new_tree')
    
    data={
        "user_id" : session["user_id"],
        "species": request.form['species'],
        "location": request.form['location'],
        "reason": request.form['reason'],
        "date_planted": request.form['date_planted'],
    }
    Tree.save_tree(data)
    return redirect('/dashboard')

@app.route('/dashboard/view_tree/<int:tree_id>')
def view_tree(tree_id):
    if not 'user_id' in session: 
        flash('log in')
        return redirect('/')
    tree_data = { "id": tree_id}
    tree = Tree.get_tree_with_user(tree_data)

    data= { "id": session['user_id']}
    user = User.get_one(data)

    return render_template('view_tree.html', tree=tree, user= user)

@app.route('/dashboard/my_trees')
def usersTree():
    data = {
        "id": session["user_id"]
    }
    user =User.get_user_tree(data)

    return render_template('my_trees.html',user=user)


@app.route('/edit/<int:tree_id>')
def tree_edit(tree_id):
    if not 'user_id' in session: 
        flash('Must be logged in')
        return redirect('/')
    data = {'id': tree_id,}
    tree =  Tree.get_tree(data)


    user_data = {'id': session['user_id']}
    user = User.get_one(user_data)

    return render_template('edit.html', tree=tree, user=user)

@app.route('/update/<int:tree_id>', methods=['POST'])
def update(tree_id):
    if not 'user_id' in session: 
        flash('Must be logged in', 'logout')
        return redirect('/')
    if not Tree.validate_tree(request.form):
        return redirect(f'/edit/{tree_id}')
    data = {
        'id': tree_id,
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'user_id': session['user_id'],
    }
    Tree.update(data)
    return redirect('/dashboard')




@app.route('/dashboard/view_tree/<int:id>/destroy')
def destroy_tree(id):

    print(id)
    data = { "id": id}
    Tree.destroy(data)

    return redirect('/dashboard')
