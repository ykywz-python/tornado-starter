from tornado.web import url

from src.controllers.home_controller import HomeHandler
from src.controllers.post_controller import (
    PostListHandler, PostCreateHandler, PostEditHandler, PostDeleteHandler
)

url_patterns = [
    url(r"/", HomeHandler, name="index"),
    
    # Crud Example
    url(r"/posts", PostListHandler, name="post_list"),
    url(r"/post/new", PostCreateHandler, name="post_create"),
    url(r"/post/(\d+)", PostEditHandler, name="post_edit"),
    url(r"/post/(\d+)/delete", PostDeleteHandler, name="post_delete"),


]