from src.controllers.base_controller import BaseHandler

class AboutHandler(BaseHandler):
    def get(self):
        self.render("about.html")