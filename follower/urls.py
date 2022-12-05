from django.urls import path
from follower import views

urlpatterns = [
    path("followers/", views.FollowerList.as_view(), name="get_follower"),
    path("followers/<int:pk>/", views.FollowerDetail.as_view(),
         name="get_followers"),
]
