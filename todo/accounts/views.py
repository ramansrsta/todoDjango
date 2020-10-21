from django.shortcuts import render, redirect

from .models import UserProfileModel, Todo
from .forms import UserDetailsForm, UserProfileDetailsForm,UserLoginForm, AddTodo

from django.contrib.auth import get_user_model, authenticate,login,logout
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required
def user_register_view(request):
    if request.method == 'POST':
        form1 = UserDetailsForm(request.POST)
        form2 = UserProfileDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print(form1.data)
            print(form2.data)
            user = User(
                first_name = form1.cleaned_data['first_name'],
                last_name = form1.cleaned_data['last_name'],
                username = form1.cleaned_data['username'],
                password = form1.cleaned_data['password']
            )
            user.save()
            user.set_password(form1.cleaned_data['password'])
            user.userprofilemodel.bio = form2.cleaned_data['bio']
            user.userprofilemodel.dob = form2.cleaned_data['dob']
            user.save()
            return redirect('/accounts/login/')
    elif request.method == 'GET':
        form1 = UserDetailsForm()
        form2 = UserProfileDetailsForm()
    return render(request,'accounts/register.html', { 
        'form1' : form1,
        'form2' : form2 })

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('/accounts/index/')
    elif request.method == 'GET':
        form = UserLoginForm()
    return render(request,'accounts/login.html',{'form' : form })


@method_decorator(login_required,name='dispatch')
class IndexPageView(TemplateView):
    template_name = 'accounts/index.html'

@method_decorator(login_required,name='dispatch')
class UserLogoutView(LogoutView):
    next_page = '/accounts/login/'

@method_decorator(login_required,name='dispatch')
class AddTodoView(CreateView):
    model = Todo
    form_class = AddTodo
    template_name = 'accounts/addTodo.html'
    success_url = '/accounts/view/'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class TodoListView(ListView):
    model = Todo
    template_name = 'accounts/viewTodo.html'
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user.id)

@method_decorator(login_required,name='dispatch')
class UpdateTodo(UpdateView):
    model = Todo
    form_class = AddTodo
    template_name = 'accounts/editTodo.html'
    success_url = '/accounts/view/'

@method_decorator(login_required,name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = '/accounts/view/'
    template_name = 'accounts/viewTodo.html'
    


    

