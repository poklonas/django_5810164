from django.conf.urls import url

from . import views

app_name = 'accounting'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_user_page/$', views.add_user_page, name='add_user_page'),
    url(r'^delete_user_page/$', views.DeleteUser.as_view(), name='delete_user_page'),

    url(r'^(?P<pk>[0-9]+)/DeleteListPage/$', views.DeleteListPage.as_view(), name='DeleteListPage'),
    url(r'^(?P<pk>[0-9]+)/delete_book_page/$', views.DeleteBookPage.as_view(), name='delete_book_page'),
    url(r'^(?P<pk>[0-9]+)/add_book_page/$', views.AddBookPage.as_view(), name='add_book_page'), 
    url(r'^(?P<pk>[0-9]+)/user_book/$', views.UserBook.as_view(), name='user_book'),
    url(r'^(?P<pk>[0-9]+)/book_detail/$', views.BookDetail.as_view(), name='book_detail'), # show all list in a book
    url(r'^(?P<pk>[0-9]+)/AddList/$', views.AddList.as_view(), name='AddList'),
    url(r'^(?P<pk>[0-9]+)/TypeManage/$', views.TypeManage.as_view(), name="type_manage"), # add or delete tpye

    url(r'^func_add_user/$', views.func_add_user, name='add_user_func'),
    url(r'^(?P<list_id>[0-9]+)/func_delete_list/$', views.func_delete_list, name='func_delete_list'),
    url(r'^(?P<user_id>[0-9]+)/func_delete_user/$', views.func_delete_user, name='func_delete_user'),
    url(r'^(?P<user_id>[0-9]+)/func_add_type/$', views.func_add_type, name='func_add_type'),
    url(r'^(?P<user_id>[0-9]+)/func_add_book/$', views.func_add_book, name='func_add_book'),
    url(r'^(?P<book_id>[0-9]+)/func_add_list/$', views.func_add_list, name='func_add_list'),
    url(r'^(?P<book_id>[0-9]+)/func_delete_book/$', views.func_delete_book, name='func_delete_book'),
    url(r'^(?P<type_id>[0-9]+)/func_delete_type/$', views.func_delete_type, name='func_delete_type'),

    #special
    url(r'^(?P<book_id>[0-9]+)/list_in_date/$', views.ListInDate, name='list_in_date'),
    url(r'^(?P<book_id>[0-9]+)/download_data/$', views.save_data, name='save_data'),
    url(r'^(?P<book_id>[0-9]+)/upload_csv_page/$', views.upload_csv_page, name='upload_csv_page'),
    url(r'^(?P<book_id>[0-9]+)/func_upload_csv/$', views.upload_csv, name='func_upload_csv'),
]
