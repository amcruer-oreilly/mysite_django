# import render shortcut
from django.shortcuts import render, get_object_or_404

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
    # get the question object or return a 404 error
    question = get_object_or_404(Question, pk=question_id)
    # render the detail.html template with the question object
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)