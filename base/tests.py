# from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_task(self):
        response = self.client.post(reverse('tasks-create'), data={'title': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # Check if task creation redirects
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Test Task')

    def test_delete_task(self):
        task = Task.objects.create(user=self.user, title='Existing Task')
        response = self.client.post(reverse('tasks-delete', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Check if task deletion redirects
        self.assertEqual(Task.objects.count(), 0)

    def test_update_task(self,):
        task = Task.objects.create(user=self.user, title='Existing Task')
        response = self.client.post(reverse('tasks-update', args=[task.id]), data={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 302)  # Check if task update redirects
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')
    
