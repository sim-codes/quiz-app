from django.contrib import admin
from .models import Course, Question, Answer

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor', 'created_at', 'updated_at')
    search_fields = ('name', 'tutor__username')


class AnswerAdmin(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    list_display = ('question', 'course', 'created_at', 'updated_at')
    search_fields = ('question', 'course__name')


admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)