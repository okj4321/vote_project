from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question,Choice

# Create your views here.

def vote(request):
    # choices = Choice.objects.filter(request.choice_text).values_list()
    # if(choice == Choice.object.filter(request.choice_text))
    #     choice.choice_text = request.
    #     choice.votes = choice.votes + 1
    #     choice.question = request.question
    questions = Question.objects
    return render(request, 'vote/vote.html', {'questions': questions})

def vote_vote(request,question_text):
    question_text = get_object_or_404(Question, pk=question_text)
    return render(request, 'vote/vote_vote.html')


def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote/detail.html', {'question': question_detail})

def new(request):
    return render(request,'vote/new.html')

def voteCreate(request):
    question = Question()
    question.pub_date = timezone.datetime.now()
    question.question_text1 = request.GET['question_text_first']
    question.question_text2 = request.GET['question_text_second']
    question.save()
    return redirect('/vote/' + str(question.id))