from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}"


class Subject(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=15)

    def __str__(self):
        return f"{self.name}"


class Techsub(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return f"{self.subject_id}  {self.teacher_id}"