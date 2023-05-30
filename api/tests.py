# from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from base.models import Task

class TaskListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_retrieve_task_list(self):
        response = self.client.get('/api/tasks/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['tasks']), 0)

    def test_create_task(self):
        data = {'title': 'Test Task', 'description': 'This is a test task.'}
        response = self.client.post('/api/tasks/user/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')
        self.assertEqual(response.data['description'], 'This is a test task.')
        self.assertEqual(response.data['user'], self.user.id)

class CustomTokenObtainPairViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_obtain_token_pair(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)	


