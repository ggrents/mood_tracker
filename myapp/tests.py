import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from .views import *
from .serializers import *


class UserTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='pass12341234')

    def test_create_user(self):
        url = '/api/auth/users/'

        data = {'username': 'TestUser2', "password": "pass12341234"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_login_user(self):
        url = '/auth/token/login'
        data = {"username": "TestUser", "password": "pass12341234"}
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content)
        auth_token = response_data.get('auth_token')

        self.assertIsNotNone(auth_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryTests(APITestCase) :
    def setUp(self) :
        self.user = User.objects.create_user(username='TestUser', password='pass12341234')
        url = '/auth/token/login'
        data = {"username": "TestUser", "password": "pass12341234"}
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content)
        self.auth_token = response_data.get('auth_token')

    def test_create_category(self):
        url = reverse('category-create')
        data = {'name': 'NewCategory'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_category(self):
        data = {'name': 'NewCategory'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(reverse('category-create'), data, format='json', headers=headers)
        url = reverse('category-list')
        headers = {'Authorization': f'Token {self.auth_token}'}
        response = self.client.get(url, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 1)
        cat_name = response_data[0].get('name')
        self.assertEqual(cat_name , 'NewCategory')

    def test_detail_category(self):
        data = {'name': 'NewCategory'}
        data2 = {'name': 'NewCategory2'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(reverse('category-create'), data, format='json', headers=headers)
        self.client.post(reverse('category-create'), data2, format='json', headers=headers)
        url = reverse('category-detail', args=[1])
        response = self.client.get(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'NewCategory')

        url = reverse('category-detail', args=[2])
        response = self.client.get(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'NewCategory2')


        data = {"name" : "UpdateCategory"}
        response = self.client.put(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'UpdateCategory')

        response = self.client.delete(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.content), 0)


class TaskTests(APITestCase) :
    def setUp(self) :
        self.user = User.objects.create_user(username='TestUser', password='pass12341234')
        url = '/auth/token/login'
        data = {"username": "TestUser", "password": "pass12341234"}
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content)
        self.auth_token = response_data.get('auth_token')

    def test_create_task(self):
        data = {'name': 'NewCategory2'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(reverse('category-create'), data, format='json', headers=headers)


        url = reverse('task-create')
        data = {
    "name": "Do homework",
    "is_done": False,
    "deadline": "2024-02-24T15:30:00+03:00",
    "category": 1
}
        headers = {'Authorization': f'Token {self.auth_token}'}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_category(self):
        data = {'name': 'NewCategory'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(reverse('category-create'), data, format='json', headers=headers)

        url = reverse('task-create')
        data = {
            "name": "Do homework",
            "is_done": False,
            "deadline": "2024-02-24T15:30:00+03:00",
            "category": 1
        }
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(url, data, format='json', headers=headers)


        url = reverse('task-list')
        response = self.client.get(url, format='json',  headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        task_name = response_data[0].get('name')
        task_isdone = response_data[0].get('is_done')
        self.assertEqual(task_name , 'Do homework')
        self.assertFalse(task_isdone)


    def test_detail_task(self):
        data = {'name': 'NewCategory'}
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(reverse('category-create'), data, format='json', headers=headers)

        url = reverse('task-create')
        data = {
            "name": "Do homework",
            "is_done": False,
            "deadline": "2024-02-24T15:30:00+03:00",
            "category": 1
        }
        headers = {'Authorization': f'Token {self.auth_token}'}
        self.client.post(url, data, format='json', headers=headers)



        url = reverse('task-detail', args=[1])

        response = self.client.get(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'Do homework')

        data2 = {
            "name": "Brush teeth",
            "is_done": False,
            "deadline": "2024-02-24T15:30:00+03:00",
            "category": 1
        }
        url = reverse('task-create')
        self.client.post(url, data2, format='json', headers=headers)



        url = reverse('task-detail', args=[2])
        response = self.client.get(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'Brush teeth')


        data = {"name" : "UpdatedTask"}
        response = self.client.patch(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'UpdatedTask')

        response = self.client.delete(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.content), 0)

