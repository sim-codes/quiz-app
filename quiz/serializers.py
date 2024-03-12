from rest_framework import serializers
from .models import Quiz, QuizResult
from question.serializers import CourseSerializer

class QuizSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['title', 'course', 'duration', 'total_marks', 'no_of_questions', 'instructions', 'due_date', 'expiry_date', 'status']


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['quiz', 'marks', 'time_taken', 'date']
