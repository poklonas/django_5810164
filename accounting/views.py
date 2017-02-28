import time
import csv
import os
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Pass_book, List, List_type, Imported_csv
from django.core.files.storage import FileSystemStorage
from .forms import ImportCsvForm


class IndexView(generic.ListView): #for show home page that show all user
    model = User
    template_name = 'accounting/index.html'
    context_object_name = 'user_list'

class DeleteUser(generic.ListView):
    model = User
    template_name = 'accounting/delete_user_page.html'
    context_object_name = 'user_list'

class UserBook(generic.DetailView): # for show all user book
    model = User
    template_name = 'accounting/user_book_page.html'


class AddBookPage(generic.DetailView): # for add or delete book
    model = User
    template_name = 'accounting/add_book_page.html'

class DeleteBookPage(generic.DetailView):
    model = User
    template_name = 'accounting/delete_book_page.html'


class BookDetail(generic.DetailView): # show all list in a book
    model = Pass_book
    template_name = 'accounting/book_detail.html'


class AddList(generic.DetailView): # go to add list page
    model = Pass_book
    template_name = 'accounting/add_list_page.html'


class DeleteListPage(generic.DetailView):
    model = Pass_book
    template_name = 'accounting/delete_list_page.html'


class TypeManage(generic.DetailView): # go to add or delete type page
    model = User
    template_name = 'accounting/type_manage.html'


def add_user_page(request): # go to add user page
    return render(request, 'accounting/add_user_page.html')

def func_add_user(request): # function add user and return to main page
    text_name = request.POST.get('user_name')
    new_user = User(user_name = text_name, founded=timezone.now())
    new_user.save()
    return HttpResponseRedirect(reverse('accounting:user_book', args=[str(new_user.id)]))

def func_delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('accounting:delete_user_page'))

def func_add_book(request, user_id): # add a book to a user
    pass_book_name = request.POST.get('book_name') # get name of pass book from input
    user = User.objects.get(pk=user_id) # get user by using user_id 
    user.pass_book_set.create(book_name=pass_book_name, founded=timezone.now()) # make new pass book for user
    return HttpResponseRedirect(reverse('accounting:user_book', args=[user_id])) 

def func_delete_book(request, book_id): # delete book and any list in that book
    book = Pass_book.objects.get(pk=book_id)
    user_id = book.user.id
    book.delete()
    return HttpResponseRedirect(reverse('accounting:delete_book_page', args=[user_id],))

def func_add_list(request, book_id): # add a list to a book
    # get input from user sended
    list_name_in = request.POST.get('list_name')
    list_detail_in = request.POST.get('detail')
    list_value_in = request.POST.get('value')
    list_type_in = request.POST.get('type_text')
    list_type_for_in = request.POST.get('type_for')
    list_date_in = request.POST.get('date') 
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
    check_balance_book(book.id)
    return HttpResponseRedirect(reverse('accounting:book_detail', args=[book.id]))


def func_add_type(request, user_id): # add a type to a user
    user = User.objects.get(pk=user_id) # find user object by user_id
    type_name_in = request.POST.get('type_name')  # get input typename
    type_detail_in = request.POST.get('detail') # get input detail
    type_for_in = request.POST.get('type_for') # get input type_for
    user.list_type_set.create(type_name=type_name_in,\
                                  type_detail=type_detail_in,\
                                  type_for=type_for_in) # make new list type
    return HttpResponseRedirect(reverse('accounting:type_manage', args=[user_id]))


def func_delete_type(request, type_id): # delete type and any list that type name like that
    selected_type = List_type.objects.get(pk=type_id)
    user_id = selected_type.user.id
    selected_type.delete()
    check_balance_user(user_id)
    return HttpResponseRedirect(reverse('accounting:type_manage', args=[user_id]))

def func_delete_list(request, list_id):
    list_in = List.objects.get(pk=list_id)
    book = list_in.pass_book
    book_id = book.id
    list_in.delete()
    check_balance_book(book_id)
    return HttpResponseRedirect(reverse('accounting:DeleteListPage', args=[book_id]))

def ListInDate(request, book_id):
    pass_book = Pass_book.objects.get(pk=book_id)
    date = request.POST.get('date')
    if(date != None):
        date_in = request.POST.get('date')
    else:
        date_in = time.strftime("%Y-%m-%d")
    return render(request, 'accounting/frame_show_list.html',{
             'pass_book':pass_book, 
             'date_in':date_in,
            })

def check_balance_book(book_id):
    book = Pass_book.objects.get(pk=book_id)
    balance = 0
    list_all = List.objects.filter(pass_book=book_id)
    for list_in in list_all :
        if(list_in.list_type.type_for == 'income'):
            balance += list_in.value
        else:
            balance -= list_in.value
    book.set_balance(balance)
    book.save()

def check_balance_user(user_id):
    user = User.objects.get(pk=user_id)
    book_all = Pass_book.objects.filter(user=user_id)
    for book in book_all :
        book = Pass_book.objects.get(pk=book.id)
        balance = 0
        list_all = List.objects.filter(pass_book=book.id)
        for list_in in list_all :
            if(list_in.list_type.type_for == 'income'):
                balance += list_in.value
            else:
                balance -= list_in.value
        book.set_balance(balance)
        book.save()

def save_data(request, book_id):
    date_input = request.POST.get('date')
    if date_input != None:
    	all_list = List.objects.filter(date=date_input, pass_book=book_id)
    else:
        all_list = List.objects.filter(pass_book=book_id)
    response = HttpResponse(content_type='text/csv') # set type for not return as html
    response['Content-Disposition'] = 'attachment; filename="all_list_data.csv"' # file name
    # start write #
    field = ['Year', 'Month', 'Day', 'Detail', 'Type', 'Income', 'Expenses'] # head
    writer = csv.DictWriter(response, fieldnames=field)
    writer.writeheader() # write head
    for a_list in all_list:
        if a_list.list_type.type_for == 'income':
            writer.writerow({'Year' : a_list.get_year(),
                             'Month' : a_list.get_month(),
                             'Day' : a_list.get_day(),
                             'Detail' : a_list.list_name,
                             'Type' : a_list.list_type.type_name,
                             'Income' : a_list.value})
        else:
            writer.writerow({'Year' : a_list.get_year(),
                             'Month' : a_list.get_month(),
                             'Day' : a_list.get_day(),
                             'Detail' : a_list.list_name,
                             'Type' : a_list.list_type.type_name,
                             'Expenses' : a_list.value})
    # stop write #
    return response

def upload_csv_page(request, book_id):
    form = ImportCsvForm()
    return render(request, 'accounting/upload_csv_page.html', {'form': form, 'book_id': book_id})

def upload_csv(request, book_id):
    if request.method == 'POST':
        form = ImportCsvForm(request.POST, request.FILES)
        if form.is_valid():
            csv_object = form.save()
            update_from_csv(csv_object, book_id)
            return HttpResponseRedirect(reverse('accounting:book_detail', args=[book_id]))
    else:
        form = ImportCsvForm()
    return render(request, 'accounting:upload_csv_page', {'form': form})

def update_from_csv(imported_csv, book_id):
    path = imported_csv.get_csv_file()
    book = Pass_book.objects.get(pk=book_id)
    with open(path, 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            year = row['Year']
            month = row['Month']
            day = row['Day']
            date = year + '-' + month + '-' + day
            detail_in = row['Detail']
            if (row['Income'] != ''):
                value_in = row['Income']
                type_for_in = 'income'
            else:
                value_in = row['Expenses']
                type_for_in = 'expenses'
            type_in = row['Type']
            try:
                list_type = List_type.objects.get(type_name=type_in, type_for=type_for_in)
            except:
                user = User.objects.get(pk=book.user.id) # get user object by use use_id
                user.list_type_set.create(type_name=type_in,\
                                          type_for=type_in)     # make new list_type
                list_type = List_type.objects.get(type_name=type_in, type_for=type_for_in)
            test= book.list_set.create( list_type=list_type,\
                                  list_name=detail_in,\
                                  detail='',\
                                  value=value_in,\
                                  date=date,\
                                      )
    check_balance_user(book.user.id)
    print("Data Base has been Updated by Import CSV file")
    
