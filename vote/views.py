from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question

# Create your views here.

def vote(request):
    questions = Question.objects
    return render(request, 'vote/vote.html', {'questions': questions})

def vote_vote1(request,question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    question_detail.votes_qestion1 = question_detail.votes_qestion1+1
    question_detail.save()
    return render(request, 'vote/vote_vote.html',{'question': question_detail})

def vote_vote2(request,question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    question_detail.votes_qestion2 = question_detail.votes_qestion2+1
    question_detail.save()
    return render(request, 'vote/vote_vote.html',{'question': question_detail})

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