from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt        
from flask_app import app
from flask_app.models import user
bcrypt = Bcrypt(app) 



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile( "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
class Tree:

    db = "arbortrary_db"

    def __init__(self,data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data ['date_planted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    

    @classmethod
    def save_tree(cls,data):
        query = "INSERT INTO trees (user_id, species, location, reason, date_planted) values (%(user_id)s, %(species)s,%(location)s,%(reason)s, %(date_planted)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod 
    def get_all_tree(cls):
        query = "SELECT * from trees;"

        results = connectToMySQL(cls.db).query_db(query)

        trees = []

        for band in results:
            trees.append(cls(band))
        return trees

    @classmethod
    def get_tree(cls, data):
        query = 'SELECT * FROM trees WHERE trees.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results: 
            return False
        else:
            return cls(results[0])

    def get_one(cls,data):
        query = "SELECT * from trees where trees.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)

        return (cls(results[0]))
    @classmethod
    def get_tree_with_user(cls, data):
        query = 'SELECT * FROM trees JOIN users ON trees.user_id = users.id WHERE trees.id = %(id)s'
        results = connectToMySQL(cls.db).query_db(query, data)
        tree = cls(results[0])
        user_data = {
            'id' : results[0]['users.id'],
            'first_name' :results [0]['first_name'],
            'last_name' :results [0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        planter = user.User(user_data)
        tree.user = planter
        return tree

    @classmethod
    def trees_users(cls):
        query = 'SELECT * FROM trees JOIN users ON trees.user_id = users.id'
        results = connectToMySQL(cls.db).query_db(query)
        all_trees = []

        for tree in results:
            new_tree = cls(tree)
            user_data = {
            'id' : tree['users.id'],
            'first_name' : tree['first_name'],
            'last_name' : tree['last_name'],
            'email' : tree['email'],
            'password' : tree['password'],
            'created_at' : tree['users.created_at'],
            'updated_at' : tree['users.updated_at']
        }
            planter = user.User(user_data)
            new_tree.user = planter
            all_trees.append(new_tree)
        return all_trees



    @classmethod 
    def get_users_tree(cls,data):

        query ="select * from users LEFT JOIN trees on trees.user_id = users.id where users.id =%(id)s;"

        results = connectToMySQL(cls.db).query_db(query,data)

        trees =[]
        for tree in results:
            trees.append(cls(tree))
        return trees

    @classmethod
    def update(cls, data):
        query = 'UPDATE trees SET species = %(species)s, location = %(location)s, reason = %(reason)s, date_planted = %(date_planted)s, updated_at = NOW() WHERE trees.id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)    
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE from trees where trees.id = %(id)s;"

        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_tree(data):
        is_valid = True

        if len(data['species']) < 3:
            flash("Enter Species Name.")
            is_valid = False
        if len(data['location']) < 3:
            flash("Enter Location")
            is_valid = False
        if len(data['reason']) < 3:
            flash("Enter Reason")
            is_valid = False
        if len(data['date_planted']) <1:
            flash("Select a Date")
            is_valid = False
        return is_valid


