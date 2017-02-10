from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Question, choice
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'bmi/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:20]

class DeleteQuestionPage(generic.ListView):
	template_name = 'bmi/delete_question_page.html'
	context_object_name = 'question_list'
	model = Question

class DetailView(generic.DetailView):
    model = Question
    template_name = 'bmi/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'bmi/result.html'

class ChoiceManage(generic.DetailView):
	model = Question
	template_name = 'bmi/choice_manage.html'

def new_question(request):
	return render(request, 'bmi/new_question.html')

def add_question(request):
	question_text = request.POST.get('question_text')
	new_question = Question(question_text=question_text, pub_date=timezone.now())
	new_question.save()
	return HttpResponseRedirect(reverse('bmi:choice_manage', args=(new_question.id,)))

def add_choice(request, question_id):
	new_choice_text = request.POST.get('new_choice')
	question = Question.objects.get(pk=question_id)
	question.choice_set.create(choice_text=new_choice_text, votes=0)
	return HttpResponseRedirect(reverse('bmi:choice_manage', args=(question.id,)))

def delete_choice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request, 'bmi/choice_manage.html',{
			 'question':question, 
			 'error_message':"You didn't select a choice.",
			})
	else:
		selected_choice.delete()
	return HttpResponseRedirect(reverse('bmi:choice_manage', args=(question.id,)))

def delete_question(request):
	question = get_object_or_404(Question, pk=request.POST['question_select'])
	choice_all = question.choice_set.all()
	choice_all.delete()
	question.delete()
	return HttpResponseRedirect(reverse('bmi:delete_question_page'))
	
	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'bmi/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('bmi:results', args=(question.id,)))
