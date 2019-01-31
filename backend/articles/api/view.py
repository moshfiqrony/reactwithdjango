from rest_framework import viewsets

from ..models import Article
from .serilizers import ArticleSerializer

class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer