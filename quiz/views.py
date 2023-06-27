from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from quiz.forms import SignUpForm
from .models import *
import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Question, Result


# Create your views here.
def home(request):
	return render(request,'base.html',{})
def LoginView(request):
	return render(request,'login.html',{})

# @method_decorator(login_required, name='dispatch')
# class Mainview(View):
#     def get(self, request):
#         q =list( Question.objects.all())
#         random.shuffle(q)
#         for question in q:
#             answers = list(question.question_answer.all())
#             random.shuffle(answers)
#             question.shuffled_answers = answers
#         return render(request, "main.html", {"questions": q})


class Mainview(View):
    def get(self, request):
        questions = list(Question.objects.all())
        random.shuffle(questions)

        for question in questions:
            answers = list(question.question_answer.all())
            random.shuffle(answers)
            question.shuffled_answers = answers

        context = {
            'questions': questions
        }

        return render(request, 'main.html', context)

    def post(self, request):
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0

        for question in questions:
            total += 1
            selected_answer_id = request.POST.get(f'question_{question.pk}')
            selected_answer = question.question_answer.get(pk=selected_answer_id) if selected_answer_id else None

            if selected_answer and selected_answer.is_correct:
                score += question.marks
                correct += 1
            else:
                wrong += 1

        percent = (score / (total * questions[0].marks)) * 100 if total > 0 else 0

        result = Result.objects.create(user=request.user, marks=score)

        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'result': result,
        }

        return render(request, 'result.html', context)


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

def UserLogin(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']

        #Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"Login successfully")
			return redirect('Mainview')
		else:
			messages.success(request,"Error occure please try again")
			return redirect('userLogin')
	else:
		return render(request,'login.html')
	
def UserLogout(request):
	logout(request)
	messages.success(request," You have been Loggedout..!!!.")
	return redirect('home')


def quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0

        for question in questions:
            total += 1
            selected_answer_id = request.POST.get(f'question_{question.pk}')  # Assuming the form field names are "question_<question_id>"
            selected_answer = question.question_answer.get(pk=selected_answer_id) if selected_answer_id else None

            if selected_answer and selected_answer.is_correct:
                score += question.marks
                correct += 1
            else:
                wrong += 1

        percent = (score / (total * question.marks)) * 100 if total > 0 else 0

        result = Result.objects.create(user=request.user, marks=score)

        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'result': result,
        }

        return render(request, 'Quiz/result.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/abc.html', context)
