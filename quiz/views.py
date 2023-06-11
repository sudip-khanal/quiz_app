from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from quiz.forms import SignUpForm
from .models import *
import random


# Create your views here.
def home(request):
	return render(request,'base.html',{})

class Mainview(View):
    def get(self, request):
        q =list( Question.objects.all())
        random.shuffle(q)
        #a = Answer.objects.filter(Question.uid)
        for question in q:
            answers = list(question.question_answer.all())
            random.shuffle(answers)
            question.shuffled_answers = answers
        return render(request, "main.html", {"questions": q})

# user registration
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			# username = form.cleaned_data['username']
			# password = form.cleaned_data['password1']
			# user = authenticate(username=username, password=password)
			# login(request, user)
			# messages.success(request, 'Admin has been registered Successfully!!')
            # return redirect('adminpage')
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('main')
	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form':form})

	return render(request, 'signup.html', {'form':form})

