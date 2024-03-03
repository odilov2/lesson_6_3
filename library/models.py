from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=12)
    group_number = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.book_id}  {self.student_id}"