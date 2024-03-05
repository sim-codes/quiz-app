from django.urls import path
from .views import (QuizListCreateView,
                    QuizView,
                    TakeQuizView,
                    QuizResultView,)

app_name = 'quiz'

urlpatterns = [
    path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),
    path('quiz/', QuizListCreateView.as_view(), name='create-list-quiz'),
    path('take-quiz/<int:pk>/', TakeQuizView.as_view(), name='take-quiz'),
    path('quiz-result/', QuizResultView.as_view(), name='quiz-result'),
]