from django.urls import path
from .views import (
    user_login_view, user_register_view,
    IndexPageView, UserLogoutView, 
    AddTodoView,TodoListView,
    UpdateTodo, TodoDeleteView)
app_name = 'accounts'


urlpatterns = [
    path('login/', user_login_view, name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('register/', user_register_view, name="register"),
    path('index/', IndexPageView.as_view(), name="index"),
    path('add/', AddTodoView.as_view(), name="add"),
    path('view/', TodoListView.as_view(), name="view"),
    path('update/<int:pk>/', UpdateTodo.as_view(), name="update"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="delete"),
]
