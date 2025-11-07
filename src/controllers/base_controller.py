import tornado.web
import logging

from src.config.const import APP_NAME

class BaseHandler(tornado.web.RequestHandler):
    def get_flash_message(self):
        """
        Gets and clears the flash message from the secure cookie.
        """
        message = self.get_secure_cookie("flash_message")
        if message:
            self.clear_cookie("flash_message")
            return message.decode('utf-8')
        return None

    def set_flash_message(self, message):
        """
        Sets a flash message in a secure cookie.
        """
        self.set_secure_cookie("flash_message", message)

    def set_page_title(self, title):
        self.page_title = title
    
    def set_with_out_header(self, value):
        self.with_out_header = value        
    
    def render(self, template_name, **kwargs):
        kwargs['app_name'] = APP_NAME
        kwargs['page_title'] = getattr(self, 'page_title', APP_NAME)      
        kwargs['with_out_header'] = getattr(self, 'with_out_header', False)          

        kwargs['current_path'] = self.request.path
        kwargs['flash_message'] = self.get_flash_message()

        super().render(template_name, **kwargs)

    def write_error(self, status_code, **kwargs):
        """
        Override to log errors and render a custom 500 page.
        """
        if 'exc_info' in kwargs:
            # Log the full exception traceback
            logging.error(
                f"Uncaught exception for {self.request.method} {self.request.uri}",
                exc_info=kwargs['exc_info']
            )

        if not self.settings.get("debug"):
            self.render("500.html")
        else:
            # In debug mode, let Tornado render the default error page with the traceback
            super().write_error(status_code, **kwargs)