from django.contrib import admin
from .models import *

# Register your models here.


class AnswerAdmin(admin.StackedInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Category)
