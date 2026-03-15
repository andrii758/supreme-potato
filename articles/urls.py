from django.urls import path

from .views import ArticleDetailView

urlpatterns = [
        path("<int:pk>/detail/", ArticleDetailView.as_view(), name="article_detail"),
    ]
