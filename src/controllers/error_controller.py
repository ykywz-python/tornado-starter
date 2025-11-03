from src.controllers.base_controller import BaseHandler

class Error404Handler(BaseHandler):
    def prepare(self):
        """Override to handle 404 errors."""
        self.set_status(404)
        self.render("404.html")