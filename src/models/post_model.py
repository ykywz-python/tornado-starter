from tinydb import Query

class PostModel:
    def __init__(self, db):
        self.db = db

    def all(self):
        return self.db.all()

    def get(self, post_id):
        return self.db.get(doc_id=post_id)

    def create(self, title, content):
        return self.db.insert({'title': title, 'content': content})

    def update(self, post_id, title, content):
        self.db.update({'title': title, 'content': content}, doc_ids=[post_id])

    def delete(self, post_id):
        self.db.remove(doc_ids=[post_id])