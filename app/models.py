from flask.ext.login import UserMixin

class User():

    def __init__(self, username, password):
        self.id = username
        self.password = password

    def get_username():
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
