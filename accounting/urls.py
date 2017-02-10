from django.conf.urls import url

from . import views

app_name = 'accounting'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_user_page/$', views.add_user_page, name='add_user_page'),
    url(r'^add_user_func/$', views.add_user_func, name='add_user_func'),
    url(r'^(?P<pk>[0-9]+)/page_add_book/$', views.BookManage.as_view(), name='book_manage'),
    url(r'^(?P<pk>[0-9]+)/user_book/$', views.UserBook.as_view(), name='user_book'),
    url(r'^(?P<pk>[0-9]+)/book_detail/$', views.BookDetail.as_view(), name='book_detail'),
    url(r'^(?P<user_id>[0-9]+)/func_add_book/$', views.func_add_book, name='func_add_book'),
]
