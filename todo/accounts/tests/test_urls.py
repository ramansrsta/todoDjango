from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import (
    user_login_view, user_register_view,
    IndexPageView, UserLogoutView, 
    AddTodoView,TodoListView,
    UpdateTodo, TodoDeleteView)

class TestUrls(SimpleTestCase):
    #testing for function based views -- login view
    def test_login_url_is_resolved(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func, user_login_view)

    #testing for class based views -- logout view
    def test_logout_url_is_resolved(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func.view_class, UserLogoutView)
    
    #testing for update view with arguments --update view
    def test_update_url_is_resolved(self):
        url = reverse('accounts:update',args=['1'])
        self.assertEquals(resolve(url).func.view_class, UpdateTodo)

    #testing for delete view of todo
    def test_delete_url_is_resolved(self):
        url = reverse('accounts:delete',args=['2'])
        self.assertEquals(resolve(url).func.view_class,TodoDeleteView)

    #testing for remaining views
    def test_register_url_is_resolved(self):
        url = reverse('accounts:register')
        self.assertEquals(resolve(url).func, user_register_view)

