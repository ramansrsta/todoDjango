from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import UserProfileModel, Todo
from django.contrib.auth.models import User
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_url = reverse('accounts:view')
        self.index_url = reverse('accounts:index')
        self.create_todo_url = reverse('accounts:add')
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def test_todo_list_view_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.view_url)
        self.assertEquals(response.status_code,200)
        # print(response['location']) checks the current location and where it will go next
        self.assertTemplateUsed(response,'accounts/viewTodo.html')
    
    def test_index_view(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/index.html')

    def test_todo_create(self):
        self.client.login(username='john',password='johnpassword')
        response = self.client.post(self.create_todo_url, {
            'user' : 1,
            'todo' : 'Yes yes',
            'created_at' : '',
            'updated_at' : ''
        })
        #self.assertTemplateUsed(response,'accounts/addTodo.html') #how to test this ??
        self.assertRedirects(response, '/accounts/view/')
        self.assertEquals(response.status_code,302)
        #print(response['location']) #good for testing purposes 
        self.assertEquals(Todo.objects.last().todo, 'Yes yes')

    def test_todo_create_without_data(self):
        self.client.login(username='john',password='johnpassword')
        response = self.client.post(self.create_todo_url,)
        self.assertEquals(Todo.objects.all().count(),0)
    
    #not completed needs work: How to do it??
    def test_todo_update_and_redirection(self):
        self.client.login(username='john',password='johnpassword')
        tododb = Todo.objects.create(
            user = self.user,
            todo = 'Yes yes',
            created_at = '',
            updated_at = ''
        )
        response = self.client.post(
            reverse('accounts:update', kwargs={'pk': tododb.id}), 
            { 
            'user' : self.user,
            'todo' : 'No No',
            'created_at' :  '',
            'updated_at' : ''
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/view/')
        tododb.refresh_from_db()
        self.assertEqual(tododb.todo, 'No No')
    



