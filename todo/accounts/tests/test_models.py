from django.test import SimpleTestCase, TestCase
from accounts.models import UserProfileModel, Todo
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
       self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
       self.todo =  Todo.objects.create(user=self.user,todo='NotTodo')


    def test_created_at_and_updated_at(self):
       self.assertEquals(self.todo.user, self.user)
       self.assertEquals(self.todo.todo, 'NotTodo')
       #self.assertEquals(self.todo.created_at, ' ')

    def test_user_profile_model(self):
       self.profile = User.objects.last().userprofilemodel
       self.assertEquals(self.profile.bio, '')
       