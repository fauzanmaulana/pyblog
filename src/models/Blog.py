class Blog:
    def __init__(self, user_id, title, desc, image, date):
        self.user_id = user_id
        self.title = title
        self.desc = desc
        self.image = image
        self.date = date

    def obj(self):
        return {"user_id" : self.user_id, "title" : self.title, "desc" : self.desc, "image" : self.image, "date" : self.date}
