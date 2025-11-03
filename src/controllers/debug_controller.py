from src.controllers.base_controller import BaseHandler

class DebugErrorHandler(BaseHandler):
    def get(self):
        # This will raise a ZeroDivisionError
        result = 1 / 0