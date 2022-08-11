from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']
        self.create_at = data['created_at']
        self.updated_at = data ['updated_at']



    @classmethod
    def save(cls,data):
        query ="INSERT INTO dojos (name, location,language, comment, created_at,updated_at)  value (%(name)s, %(location)s, %(language)s,%(comment)s, NOW(),NOW());"    
        return connectToMySQL('dojo_survey_schema').query_db(query,data)


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) <= 0:
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        if len(dojo['location']) < 1:
            flash("please select a location.")
            is_valid = False
        
        if  len(dojo['language']) < 1:
            flash("Please select a language.")
            is_valid = False
        
        if len(dojo['comment']) < 1:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid


