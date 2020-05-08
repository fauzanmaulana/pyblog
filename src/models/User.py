class User:
    def __init__(self, username, email, password, role="user"):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def obj(self):
        return {"username" : self.username, "email" : self.email, "password" : self.password, "role" : self.role}
