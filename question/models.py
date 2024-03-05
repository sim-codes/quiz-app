from django.db import models
import random
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=255)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'courses')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Question(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct})
        return data


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer