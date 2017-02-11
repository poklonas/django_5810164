from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Pass_book, Program,Type_programe, Day, Month, Year

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


class AddIncome(generic.DetailView):
    model = Pass_book
    template_name = 'accounting/income_page.html'


class AddExpenses(generic.DetailView):
    model = Pass_book
    template_name = 'accounting/expenses_page.html'


class TypeManage(generic.DetailView):
    model = User
    template_name = 'accounting/type_manage.html'


class PageAddType(generic.DetailView):
    model = User
    template_name = 'accounting/add_type.html'


class TypeDetail(generic.DetailView):
    model = Type_programe
    template_name = 'accounting/type_detail.html'


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

def func_add_income(request, book_id):
    program_name_in = request.POST.get('program_name')
    program_detail_in = request.POST.get('detail')
    program_value_in = request.POST.get('value')
    #this is assume
    program_type_in = request.POST.get('type_text')
    program_day_in = Day.objects.get(pk=1)
    program_month_in = Month.objects.get(pk=1)
    program_year_in = Year.objects.get(pk=1)
    # end assume
    book = Pass_book.objects.get(pk=book_id)
    try:
        programe_instant = Type_programe.objects.get(type_name=program_type_in)
    except:
         user = User.objects.get(pk=book.user.id)
         user.type_programe_set.create(type_name=program_type_in,\
                                       type_for="income")
         programe_instant = Type_programe.objects.get(type_name=program_type_in)
    book.program_set.create(head_program=program_name_in,\
                             detail=program_detail_in,\
                             value=program_value_in,\
                             type_programe=programe_instant,\
                             day_published=program_day_in,\
                             month_published=program_month_in,\
                             year_published=program_year_in,\
                             )
    book.balance += float(program_value_in)
    book.save()
    print(request.POST.get('date'))
    return HttpResponseRedirect(reverse('accounting:book_detail', args=(book_id)))

def func_add_expenses(request, book_id):
    program_name_in = request.POST.get('program_name')
    program_detail_in = request.POST.get('detail')
    program_value_in = request.POST.get('value')
    #this is assume
    program_type_in = request.POST.get('type_text')
    program_day_in = Day.objects.get(pk=1)
    program_month_in = Month.objects.get(pk=1)
    program_year_in = Year.objects.get(pk=1)
    # end assume
    book = Pass_book.objects.get(pk=book_id)
    try:
        programe_instant = Type_programe.objects.get(type_name=program_type_in)
    except:
         user = User.objects.get(pk=book.user.id)
         user.type_programe_set.create(type_name=program_type_in,\
                                       type_for="expenses")
         programe_instant = Type_programe.objects.get(type_name=program_type_in)
    book.program_set.create(head_program=program_name_in,\
                             detail=program_detail_in,\
                             value=program_value_in,\
                             type_programe=programe_instant,\
                             day_published=program_day_in,\
                             month_published=program_month_in,\
                             year_published=program_year_in,\
                             )
    book.balance -= float(program_value_in)
    book.save()
    return HttpResponseRedirect(reverse('accounting:book_detail', args=(book_id)))

def func_add_type(request, user_id):
    user = User.objects.get(pk=user_id)
    type_name_in = request.POST.get('type_name')
    type_detail_in = request.POST.get('detail')
    type_for_in = request.POST.get('type_for')
    user.type_programe_set.create(type_name=type_name_in,\
                                  type_detail=type_detail_in,\
                                  type_for=type_for_in)
    return HttpResponseRedirect(reverse('accounting:type_manage', args=(user_id)))
