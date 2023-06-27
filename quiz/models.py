from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=50, default="Computer")

    def __str__(self):
        return self.title


class Question(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question_answer"
    )
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    
class Result(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.marks}'

