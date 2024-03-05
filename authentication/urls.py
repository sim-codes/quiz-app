from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (StudentRegistrationView,
                    TeacherRegistrationView,
                    LogoutView,
                    MyTokenObtainPairView,
                    )


app_name = 'authentication'

urlpatterns = [
    path('register/student/', StudentRegistrationView.as_view(), name='student-registration'),
    path('register/teacher/', TeacherRegistrationView.as_view(), name='teacher-registration'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', LogoutView.as_view(), name='token_blacklist'),
]