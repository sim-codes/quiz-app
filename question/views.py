from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Question, Course, Answer
from .serializers import QuestionSerializer, CourseSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
         if request.user.is_authenticated:
             return request.user.is_teacher
         

class CourseView(ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher,)

    def get_queryset(self):
        courses = Course.objects.filter(tutor=self.request.user)
        return courses


class CourseUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher,)

    def get_queryset(self):
        courses = Course.objects.filter(tutor=self.request.user)
        return courses


class QuestionView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher)

    queryset = Question.objects.all()

    def get(self, request):
        courses = Course.objects.filter(tutor=self.request.user)
        data = []
        for course in courses:
            questions = Question.objects.filter(course=course)
            data.append({
                'course': course.name,
                'question': [{
                    'id': question.id,
                    'tutor': course.tutor.username,
                    'question': question.question,
                    'answers': question.get_answers()
                } for question in questions]
            })
        return Response(data)
    

    def create(self, request, *args, **kwargs):
        question = request.data.get('question')
        course = request.data.get('course')
        answers = request.data.get('answers')
        data = {
            'question': question,
            'course': course,
            'answers': answers
        }
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            course = Course.objects.get(id=course)
            question_obj = Question.objects.create(question=question, course=course)
            
            for ans in answers:
                Answer.objects.create(question=question_obj, answer=ans["answer"], is_correct=ans["is_correct"])
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({"message":"check your fields and try again"}, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(RetrieveDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher)

    

class AnswerView(ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsTeacher) 
