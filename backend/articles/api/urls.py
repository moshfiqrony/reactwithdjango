from .view import ArticleView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleView, basename='articles')
urlpatterns = router.urls