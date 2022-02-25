import random
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login, logout
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm

@ login_required
def favourite_list(request):
    new = Books.objects.all().filter(favourites=request.user)
    books = Books.objects.all().order_by('-pub_date')[:5]
    return render(request,
                  'favourites.html',
                  {'new': new, 'books': books})


@ login_required
def favourite_add(request, id):
    books = get_object_or_404(Books, id=id)
    if books.favourites.filter(id=request.user.id).exists():
        books.favourites.remove(request.user)
    else:
        books.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def base(request):
    books = Books.objects.all().order_by('-pub_date')[:3]
    run_book = random.sample(list(Books.objects.all()), 1)
    context = {
        'books': books,
        'run_book': run_book,
    }
    return render(request, 'base.html', context)

def books(request, pk=None):
    books = Books.objects.all()
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books,
        'page_obj': page_obj,
    }

    return render(request, 'books.html', context)


class RegisterUser(CreateView):

    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return dict(list(context.items()) + list())

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('base')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return dict(list(context.items()) + list())

    def get_success_url(self):
        return reverse_lazy('base')


def logout_user(request):
    logout(request)
    return redirect('login')