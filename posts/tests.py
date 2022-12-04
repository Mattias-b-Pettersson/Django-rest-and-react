from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        print(f"\nrunning {self}")
        User.objects.create_user(username="username", password="password")

    def test_can_list_post(self):
        user = User.objects.get(username="username")
        Post.objects.create(owner=user, title="title")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="username", password="password")
        response = self.client.post("/posts/", {"title": "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post("/posts/", {"title": "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    print("Running 'PostDetailViewTests'")
    
    def setUp(self):
        print(f"\nrunning{self}")
        User.objects.create_user(username="username", password="password")
        User.objects.create_user(username="username2", password="password")
        user = User.objects.get(username="username")
        Post.objects.create(owner=user, title="title")

    def test_user_can_retrieve_post_with_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_retrieve_post_with_invalid_id(self):       
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_post_they_own(self):
        self.client.login(username="username", password="password")
        response = self.client.put("/posts/1/", {"title": "a fantastic title"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_can_update_post_they_own(self):
        self.client.login(username="username2", password="password")
        response = self.client.put("/posts/1/", {"title": "a fantastic title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
