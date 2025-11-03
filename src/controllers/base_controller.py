import tornado.web
import logging

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

    def render(self, template_name, **kwargs):
        kwargs['flash_message'] = self.get_flash_message()
        # Pass the current request path to the template
        kwargs['current_path'] = self.request.path
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