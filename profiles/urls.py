from django.urls import path
from profiles import views

urlpatterns = [
    path("profiles/", views.ProfileList.as_view(), name="get_profiles"),
    path("profile/<int:pk>/", views.ProfileDetail.as_view(), name="get_profile")
]