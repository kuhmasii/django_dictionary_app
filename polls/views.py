from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from . models import Question, Choice
from django.urls import reverse


def index(request):
    # fetching out first five latest question from database
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by("-pub_date")[:5]

    return render(request, 'polls/index.html', dict(latest_question_list=latest_question_list))


def detail(request, question_id):
    try:
        question = Question.objects.get(
            pk=question_id, 
            pub_date__lte=timezone.now()
        )
        choice = question.choices.order_by("-id")
        # this is another way to query the choices asked when not using the argument related_names
        # choice = Choice.objects.all()
        # choice = Choice.objects.filter(question=question)
    except Question.DoesNotExist:
        raise Http404("Query or Question you are looking for not in database.")
    return render(request, 'polls/detail.html', dict(question=question, choice=choice))


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choice = question.choices.order_by("-id")
    except Question.DoesNotExist:
        raise Http404("Query or Question you are looking for not in database")
    return render(request, 'polls/results.html', dict(question=question, choice=choice))


def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choice = question.choices.all()
    except Question.DoesNotExist:
        raise Http404("Query or Question you a looking for not in database.")
    else:
        try:
            selected_choice = question.choices.get(
                pk=request.POST.get("choice"))

        except(KeyError, Choice.DoesNotExist):

            return render(request, 'polls/detail.html', dict(question=question, choice=choice,
                                                             error_message="You didn't select a choice!"))

        else:
            selected_choice.votes += 1
            selected_choice.save()

            return HttpResponseRedirect(reverse("polls:results", args=[question.id]))

            # using the shortcuts redirect
            # return redirect(reverse("polls:results", args=[question.id]), permanent=True)
