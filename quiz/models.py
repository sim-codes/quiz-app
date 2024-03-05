from django.db import models
from django.conf import settings
from question.models import Course


class QuizManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Published')
    
    def active(self):
        return self.get_queryset().filter(is_active=True)
    
    def expired(self):
        return self.get_queryset().filter(is_active=False)
    

class Quiz(models.Model):
    STATUS = (
        ('DF', 'Draft'),
        ('PB', 'Published'),
    )

    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exams')
    course = models.ForeignKey('question.Course', on_delete=models.CASCADE, related_name='exams')
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    total_marks = models.IntegerField()
    instructions = models.TextField(blank=True, null=True)
    no_of_questions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS, default='DF')
    is_active = models.BooleanField(default=False)
    
    objects = models.Manager()
    QuizManager = QuizManager()

    class Meta:
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.title


class QuizResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='students')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    total_marks = models.IntegerField()
    time_taken = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'results'

    def __str__(self):
        return f'{self.student} - {self.quiz}'
