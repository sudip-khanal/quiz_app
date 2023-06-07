from django.shortcuts import render
from django.views import View
from .models import *
import random


# Create your views here.
class Homeview(View):
    def get(self, request):
        q =list( Question.objects.all())
        random.shuffle(q)
        #a = Answer.objects.filter(Question.uid)
        for question in q:
            answers = list(question.question_answer.all())
            random.shuffle(answers)
            question.shuffled_answers = answers
        return render(request, "base.html", {"questions": q})
