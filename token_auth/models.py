from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class Courses(models.Model):
    tittle = models.CharField(max_length=100)
    rating = models.FloatField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
