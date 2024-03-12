from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from question.models import Course

class TestCourseSetup(APITestCase):
    def setUp(self):
        self.course_url = reverse('question:courses')

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            is_teacher=True,
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.course = Course.objects.create(
            name='Python',
            tutor=self.user,
            description='This is a course about Python'
        )
        return super().setUp()

    def tearDown(self):
        return super().tearDown()