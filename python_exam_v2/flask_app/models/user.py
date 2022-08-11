from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models import tree

bcrypt = Bcrypt(app) 


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile( "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
class User:

    db = "arbortrary_db"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.trees = []



    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name,email,password, created_at,updated_at) values ( %(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query ="SELECT * FROM USERS where users.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return result
        return cls(result[0])
    @classmethod
    def get_one_by_email(cls, data):
        query = 'SELECT * FROM users WHERE users.email = %(email)s'
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results: 
            return False
        else:
            return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod 
    def get_user_tree(cls, data):
        query ='SELECT * FROM users LEFT JOIN trees ON trees.user_id = users.id WHERE users.id = %(id)s'
        results = connectToMySQL(cls.db).query_db(query,data)
        user = cls(results[0])
        if results[0]['trees.id'] == None:
            return cls(results[0])
        else:
            for tree_dict in results:
                tree_data = {
                    'id' : tree_dict['trees.id'],
                    'species' : tree_dict['species'],
                    'location' : tree_dict['location'],
                    'reason' : tree_dict['reason'],
                    'date_planted' : tree_dict['date_planted'],
                    'created_at' : tree_dict['trees.created_at'],
                    'updated_at' : tree_dict['trees.updated_at'],
                    'user_id': tree_dict['user_id']
                }
                user.trees.append(tree.Tree(tree_data))
        return user
    



    @staticmethod
    def validate_form(data):
        is_valid = True
        

        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash('Password must be between 8-20 characters' )
            flash('Password must include a number' )
            flash('Password must include one upper and lower case character' )
            flash('Password must include a special character' )
            is_valid = False
        if not data['password'] == data['confirm_password']:
            flash('Password must match', 'register')
            is_valid = False
        email_data = {'email': data['email']}
        user = User.get_one_by_email(email_data)
        if user:
            flash('Email already exist')
            is_valid = False


        return is_valid
    @staticmethod
    def validate_login(data):
        is_valid = True

        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid Email")
            is_valid = False
        
        return is_valid


