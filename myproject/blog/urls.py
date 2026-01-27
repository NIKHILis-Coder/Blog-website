from django.urls import path
from .import views
urlpatterns = [
    path("", views.starting_pageView.as_view(), name="starting-page"),
    path("posts", views.postsView.as_view(), name="post-page"),
    path("posts/<slug:slug>/", views.post_detailView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
