from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Pass_book

class IndexView(generic.ListView): #for show home page that show all user
    template_name = 'accounting/index.html'
    context_object_name = 'user_list'
    model = User


class UserBook(generic.DetailView): # for show all user book
    model = User
    template_name = 'accounting/user_book_page.html'


class BookManage(generic.DetailView): # for add or delete book
    model = User
    template_name = 'accounting/book_manage.html'


class BookDetail(generic.DetailView):
    model = Pass_book
    template_name = 'accounting/book_detail.html'


def add_user_page(request): # go to add user page
	return render(request, 'accounting/add_user_page.html')

def add_user_func(request): # function add user and return to main page
    text_name = request.POST.get('user_name')
    new_user = User(user_name = text_name, founded=timezone.now())
    new_user.save()
    return HttpResponseRedirect(reverse('accounting:user_book', args=str(new_user.id)))

def func_add_book(request, user_id):
    pass_book_name = request.POST.get('book_name')
    user = User.objects.get(pk=user_id)
    user.pass_book_set.create(book_name=pass_book_name, founded=timezone.now())
    return HttpResponseRedirect(reverse('accounting:user_book', args=(user_id)))

    


