from django.urls import path
from likes import views

urlpatterns = [
    path("likes/", views.LikeList.as_view(), name="get_likes"),
    path("likes/<int:pk>/", views.LikeDetail.as_view(), name="get_like"),
]
