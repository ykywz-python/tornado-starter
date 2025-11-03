from src.controllers.base_controller import BaseHandler
from src.models.post_model import PostModel

class PostListHandler(BaseHandler):
    def get(self):
        post_model = PostModel(self.settings['db'])
        posts = post_model.all()
        self.render("posts/index.html", posts=posts)

class PostCreateHandler(BaseHandler):
    def get(self):
        self.render("posts/form.html", post=None, errors=[])

    def post(self):
        title = self.get_body_argument("title", "").strip()
        content = self.get_body_argument("content", "").strip()

        if not title or not content:
            self.render("posts/form.html", post={'title': title, 'content': content}, errors=["All fields are required."])
            return

        post_model = PostModel(self.settings['db'])
        post_model.create(title, content)
        self.set_flash_message("Post created successfully!")
        self.redirect(self.reverse_url("post_list"))

class PostEditHandler(BaseHandler):
    def get(self, post_id):
        post_model = PostModel(self.settings['db'])
        post = post_model.get(int(post_id))
        self.render("posts/form.html", post=post, errors=[])

    def post(self, post_id):
        title = self.get_body_argument("title", "").strip()
        content = self.get_body_argument("content", "").strip()

        if not title or not content:
            post = {'doc_id': post_id, 'title': title, 'content': content}
            self.render("posts/form.html", post=post, errors=["All fields are required."])
            return

        post_model = PostModel(self.settings['db'])
        post_model.update(int(post_id), title, content)
        self.set_flash_message("Post updated successfully!")
        self.redirect(self.reverse_url("post_list"))

class PostDeleteHandler(BaseHandler):
    def post(self, post_id):
        post_model = PostModel(self.settings['db'])
        post_model.delete(int(post_id))
        self.set_flash_message("Post deleted successfully.")
        self.redirect(self.reverse_url("post_list"))