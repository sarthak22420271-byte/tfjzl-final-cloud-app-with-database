from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner

# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'lesson', 'grade')  # ✅ added
    inlines = [ChoiceInline]

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')  # ✅ added
    inlines = [QuestionInline]

# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)  # ✅ added
admin.site.register(Learner)     # ✅ added
