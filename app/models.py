from flask.ext.login import UserMixin

class User():
    instances = []

    def __init__(self, user_id, first_name, last_name, email, password, username):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
        
        User.instances.append(self)

    def get_username(self):
        return self.id

    def is_authenticated():
        return True #return true if user is authenticated

    def is_active():
        return True #returns true if this is an active user

    def is_anonymous():
        return False #returns false if not a user

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return str(self.id)
