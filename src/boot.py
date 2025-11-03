import logging
import os
import tornado.web

from tinydb import TinyDB
from src.config.path import DATA_PATH, LOG_FILE, LOG_PATH, RESOURCE_PATH
from src.routes import url_patterns
from src.controllers.error_controller import Error404Handler
from src.utils.pyinstaller_ import is_frozen


class Application(tornado.web.Application):
    def __init__(self):
        # Setup paths before settings
        self.setup_folder()

        settings = {
            "template_path": os.path.join(RESOURCE_PATH, "resources", "templates"),
            "static_path": os.path.join(RESOURCE_PATH, "resources", "static"),
            "debug": True if not is_frozen() else False,
            "cookie_secret": "your-super-secret-and-long-cookie-secret-string",
            "default_handler_class": Error404Handler,
            "db": TinyDB(os.path.join(DATA_PATH, 'db.json')),
        }
        super(Application, self).__init__(url_patterns, **settings)
        
        # print("Performing boot-time operations...")

        self.setup_logging()

        # print("Boot-time operations complete.")
        
    def setup_folder(self):
        os.makedirs(DATA_PATH, exist_ok=True)
        os.makedirs(LOG_PATH, exist_ok=True)
        
        
    def setup_logging(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LOG_FILE),  # Log to a file
                logging.StreamHandler()         # Log to the console
            ]
        )
        
    def shutdown(self):
        print("Closing database connection...")
        self.settings['db'].close()
        