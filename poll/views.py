from django.shortcuts import render

# Create your views here.

from poll.models import Question, Choice


def poll_view(request, pk):

    try:
        que = Question.objects.get(id=pk)
        choices = Choice.objects.filter(question=que)

    except:
        return render(request, "404.html")

    return render(request, "poll.html", {"question": que, "choices": choices})


def home_view(request):
    ques = Question.objects.all()
    return render(request, "home.html", {"questions": ques})
