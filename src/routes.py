from tornado.web import url

from src.controllers.home_controller import HomeHandler
from src.controllers.about_controller import AboutHandler
from src.controllers.contact_controller import ContactHandler
from src.controllers.post_controller import (
    PostListHandler, PostCreateHandler, PostEditHandler, PostDeleteHandler
)
from src.controllers.debug_controller import DebugErrorHandler

url_patterns = [
    url(r"/", HomeHandler, name="index"),
    url(r"/about", AboutHandler, name="about"),
    url(r"/contact", ContactHandler, name="contact"),
    url(r"/posts", PostListHandler, name="post_list"),
    url(r"/post/new", PostCreateHandler, name="post_create"),
    url(r"/post/(\d+)", PostEditHandler, name="post_edit"),
    url(r"/post/(\d+)/delete", PostDeleteHandler, name="post_delete"),
    url(r"/debug-error", DebugErrorHandler, name="debug_error"),
]