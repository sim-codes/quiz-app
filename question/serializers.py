from rest_framework import serializers
from .models import Question, Course, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer', 'is_correct', 'question']
        lookup_field = 'question'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
   
    class Meta:
        model = Question
        fields = ['id', "course", 'question', 'answers']


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'tutor', 'description']