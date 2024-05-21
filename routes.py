from api.category import router as category_router
from api.post import router as post_router
from api.tag import router as tag_router
from api.author import router as author_router

routes_list = [
    author_router,
    category_router,
    post_router,
    tag_router,
]
