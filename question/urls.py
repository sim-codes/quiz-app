from django.urls import path
from .views import (QuestionView, 
                    CourseView, 
                    CourseUpdateView,
                    QuestionUpdateView, 
                    # QuestionCreateView, 
                    AnswerView)

app_name = 'question'

urlpatterns = [
    path('', QuestionView.as_view(), name='question'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('course/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    # path('question/', QuestionCreateView.as_view(), name='question-create'),
    path('answers/', AnswerView.as_view(), name='answer-create'),
    path('question/<int:pk>/', QuestionUpdateView.as_view(), name='question-detail'),
]