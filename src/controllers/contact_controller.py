from src.controllers.base_controller import BaseHandler

class ContactHandler(BaseHandler):
    def get(self):
        # Pass empty values on the initial GET request
        self.render("contact.html", errors=[], form_data={})

    def post(self):
        name = self.get_body_argument("name", "").strip()
        message = self.get_body_argument("message", "").strip()

        errors = []
        if not name:
            errors.append("Name is a required field.")
        if not message:
            errors.append("Message is a required field.")

        if errors:
            # Validation failed, re-render the form with errors and original data
            form_data = {"name": name, "message": message}
            self.render("contact.html", errors=errors, form_data=form_data)
            return

        # Validation succeeded: save data, set flash message, and redirect
        print(f"Received contact submission from {name}: {message}")
        self.set_secure_cookie("flash_message", f"Thank you, {name}! Your message has been received.")
        self.redirect(self.reverse_url("index"))

