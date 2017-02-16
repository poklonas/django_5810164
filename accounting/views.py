from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Pass_book, List, List_type

class IndexView(generic.ListView): #for show home page that show all user
    model = User
    template_name = 'accounting/index.html'
    context_object_name = 'user_list'


class UserBook(generic.DetailView): # for show all user book
    model = User
    template_name = 'accounting/user_book_page.html'


class BookManage(generic.DetailView): # for add or delete book
    model = User
    template_name = 'accounting/book_manage.html'


class BookDetail(generic.DetailView): # show all list in a book
    model = Pass_book
    template_name = 'accounting/book_detail.html'


class AddList(generic.DetailView): # go to add list page
    model = Pass_book
    template_name = 'accounting/add_list_page.html'


class TypeManage(generic.DetailView): # go to add or delete type page
    model = User
    template_name = 'accounting/type_manage.html'


class PageAddType(generic.DetailView): # go to add type page
    model = User
    template_name = 'accounting/add_type.html'


def add_user_page(request): # go to add user page
	return render(request, 'accounting/add_user_page.html')

def add_user_func(request): # function add user and return to main page
    text_name = request.POST.get('user_name')
    new_user = User(user_name = text_name, founded=timezone.now())
    new_user.save()
    return HttpResponseRedirect(reverse('accounting:user_book', args=[str(new_user.id)]))

def func_add_book(request, user_id): # add a book to a user
    pass_book_name = request.POST.get('book_name') # get name of pass book from input
    user = User.objects.get(pk=user_id) # get user by using user_id 
    user.pass_book_set.create(book_name=pass_book_name, founded=timezone.now()) # make new pass book for user
    return HttpResponseRedirect(reverse('accounting:user_book', args=[user_id])) 

def func_add_list(request, book_id):
    # get input from user sended
    list_name_in = request.POST.get('list_name')
    list_detail_in = request.POST.get('detail')
    list_value_in = request.POST.get('value')
    list_type_in = request.POST.get('type_text')
    list_type_for_in = request.POST.get('type_for')
    list_date_in = request.POST.get('date') 
    # start formate mm/dd/yyyy to yyyy-mm-dd
    year_in = list_date_in[6:]
    day_in = list_date_in[3:5]
    month_in = list_date_in[0:2]
    list_date_in = year_in + "-" + month_in + "-" + day_in
    # end formate to yyyy-mm-dd
    book = Pass_book.objects.get(pk=book_id) # get book by using book_id 
    try:         # try if dont have type it will make new one for use
        list_instant = List_type.objects.get(type_name=list_type_in) # have any list_type_name like input?
    except:      # no have any list_type_name like input , or other reason
         user = User.objects.get(pk=book.user.id) # get user object by use use_id
         user.list_type_set.create(type_name=list_type_in,\
                                    type_for=list_type_for_in)     # make new list_type
         list_instant = List_type.objects.get(type_name=list_type_in) 
    book.list_set.create(list_name=list_name_in,\
                             detail=list_detail_in,\
                             value=list_value_in,\
                             list_type=list_instant,\
                             date = list_date_in,\
                             )         # make new list for a book
    if(list_type_for_in == 'income'):  # check type of list if in come + balance other -
        book.balance += float(list_value_in)
    else:
        book.balance -= float(list_value_in)
    book.save()
    return HttpResponseRedirect(reverse('accounting:book_detail', args=[book.id]))


def func_add_type(request, user_id):
    user = User.objects.get(pk=user_id) # find user object by user_id
    type_name_in = request.POST.get('type_name')  # get input typename
    type_detail_in = request.POST.get('detail') # get input detail
    type_for_in = request.POST.get('type_for') # get input type_for
    user.list_type_set.create(type_name=type_name_in,\
                                  type_detail=type_detail_in,\
                                  type_for=type_for_in) # make new list type
    return HttpResponseRedirect(reverse('accounting:type_manage', args=[user_id]))
