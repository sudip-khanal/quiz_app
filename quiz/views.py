from django.shortcuts import render
from django.views import View
from .models import *


# Create your views here.
class Homeview(View):
    def get(self, request, id):
        q = Question.objects.all()
        a = Answer.objects.get(id=BaseModel.uid)
        print(q)
        return render(request, "base.html", {"questions": q, "answers": a})
