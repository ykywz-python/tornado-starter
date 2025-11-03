from src.controllers.base_controller import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        features = [
            "MVC Structure",
            "Static File Serving",
            "Template Inheritance",
            "Data from Controller to View"
        ]
        self.render("index.html", message="Hello from Tornado MVC!", items=features)