from django.contrib import admin
from django.contrib.admin import SimpleListFilter

# Register your models here.
from .models import University, Course, StudentDegree

myModels = [University]  # iterable list

admin.site.register(myModels) 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
        list_filter = ('university',)

@admin.register(StudentDegree)
class StudentDegreeAdmin(admin.ModelAdmin):
        list_filter = ('university',)