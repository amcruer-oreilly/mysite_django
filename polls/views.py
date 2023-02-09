# import render shortcut
from django.shortcuts import render

# import 404 error
from django.http import Http404

# import the Question model from polls/models.py
from .models import Question

def index(request):
    # get a list of the last five published questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # create a context dictionary
    context = {
        'latest_question_list': latest_question_list,
    }
    # render the index.html template with the context dictionary
    return render(request, 'polls/index.html', context)

# add detail, results, and vote views
def detail(request, question_id):
    # try to get the question with the given id
    try:
        question = Question.objects.get(pk=question_id)
    # if the question does not exist, raise a 404 error
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # render the detail.html template with the question
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)