from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Contact:
    db = "dolphin_schema"
    def __init__(self,db_data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.phone_number = db_data["phone_number"]
        self.city = db_data["city"]
        self.state = db_data["state"]
        # self.vip = db_data["vip"]
        self.user_id = db_data["user_id"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.user = None


    @classmethod
    def save(cls,data):
        query = "INSERT INTO contacts (name, phone_number, city, state, user_id) VALUES (%(name)s,%(phone_number)s,%(city)s,%(state)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM contacts;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_contacts = []
        for row in results:
            all_contacts.append( cls(row) )
        return all_contacts


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM contacts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE contacts SET name=%(name)s, phone_number=%(phone_number)s, city=%(city)s, state=%(state)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM contacts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_contact(contact):
        is_valid = True
        if len(contact['name']) < 2:
            is_valid = False
            flash("Contact name must be at least 2 characters","contact")
        if len(contact['phone_number']) < 10:
            is_valid = False
            flash("Phone number must be at least 10 digits","contact")
        if len(contact['city']) < 2:
            is_valid = False
            flash("City must be at least 2 characters", "contact")
        if len(contact['state']) <2:
            is_valid = False
            flash("State must be at least 2 characters", "contact")
        return is_valid