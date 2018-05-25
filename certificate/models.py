import uuid
import datetime

from django.db import models
from datetime import datetime
# Create your models here.

# University Model
class University(models.Model):
    university_name = models.CharField(max_length=200)
    university_code = models.CharField(max_length=12)
    created_at = models.DateTimeField(default=datetime.now,blank=True )

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name_plural = "University"

# Course Model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=12)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now,blank=True )
   
    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ('course_name',)

#Student Degree Model
class StudentDegree(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    academic_year = models.IntegerField
    degree_issued_on = models.DateField('date issued', default=datetime.now)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    aggregate_score = models.FloatField
    class_obtained = models.CharField(max_length=10)

    def __str__(self):
        return (self.firstname + " " + self.lastname + " (" + self.rollno + ")")


    class Meta:
        verbose_name_plural = "StudentDegree"