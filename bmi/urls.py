from django.conf.urls import url

from . import views

app_name = 'bmi'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^delete_question_page/$', views.DeleteQuestionPage.as_view(), name='delete_question_page'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<pk>[0-9]+)/choice_manage/$', views.ChoiceManage.as_view(), name='choice_manage'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<question_id>[0-9]+)/add_choice/$', views.add_choice, name='add_choice'),
    url(r'^(?P<question_id>[0-9]+)/delete_choice/$', views.delete_choice, name='delete_choice'),
	url(r'^new_question/$', views.new_question, name='new_question'),
	url(r'^add_question/$', views.add_question, name='add_question'),
	url(r'^delete_question/$', views.delete_question, name='delete_question'),
]
