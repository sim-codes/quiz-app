from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from .models import Quiz, QuizResult
from .serializers import QuizSerializer, QuizResultSerializer
from question.models import Course, Question
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from question.views import IsTeacher

class QuizView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher,)


    # def get_queryset(self):
    #     return Quiz.objects.filter(tutor=self.request.user)


class QuizListCreateView(ListCreateAPIView):
    serializer_class = QuizSerializer
    # queryset = Quiz.objects.all()

    def get_queryset(self):
        return Quiz.objects.filter(tutor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)

    def get(self, request):
        quizzes = Quiz.objects.all()
        data = []
        for quiz in quizzes:
            data.append({
                'id': quiz.id,
                'title': quiz.title,
                'course': quiz.course.name,
                'duration': quiz.duration,
                'total_marks': quiz.total_marks,
                'no_of_questions': quiz.no_of_questions,
                'instructions': quiz.instructions,
                'due_date': quiz.due_date,
                'expiry_date': quiz.expiry_date,
                'status': quiz.status
            })
        return Response(data)

class TakeQuizView(APIView):
    # queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(tutor=self.request.user)

    def get(self, request, pk):
        due_questions = self.queryset.filter(due_date__lte=timezone.now())
        expired = self.queryset.filter(expiry_date__lte=timezone.now())
        quiz = self.queryset.get(id=pk)

        if expired.contains(quiz):
            return Response({'message': 'Exam has expired'}, status=status.HTTP_400_BAD_REQUEST)
        elif due_questions.contains(quiz):
            data = {
                    'id': quiz.id,
                    'title': quiz.title,
                    'course': quiz.course.name,
                    'duration': quiz.duration,
                    'total_marks': quiz.total_marks,
                    'no_of_questions': quiz.no_of_questions,
                    'instructions': quiz.instructions,
                    'due_date': quiz.due_date,
                    'expiry_date': quiz.expiry_date,
                    'status': quiz.status
            }

            questions = Question.objects.filter(course=quiz.course)
            

            # Get all questions and answers
            quiz_data = []
            for q in questions:
                quiz_data.append({
                    'question' : q.question,
                    'answers': question.get_answers()
                    } for question in questions)
                
            data['questions'] = quiz_data[0]
            
            return Response(data)

        else:
            return Response({'message': f'Exam is not due until: {quiz.due_date.strftime("%D")}'}, status=status.HTTP_400_BAD_REQUEST)
        

class QuizResultView(ListCreateAPIView):
    serializer_class = QuizResult
    queryset = QuizResult.objects.all()

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def get(self, request):
        results = QuizResult.objects.all()
        data = []
        for result in results:
            data.append({
                'student': result.student,
                'quiz': result.quiz,
                'marks': result.total_marks,
                'time_taken': result.time_taken,
                'date': result.date
            })
        return Response(data)

