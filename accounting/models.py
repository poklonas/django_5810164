import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=60)
    founded = models.DateTimeField('date founded')

    def __str__(self):
        return self.user_name

    def was_founded_recently(self):
        return self.founded >= timezone.now() - datetime.timedelta(days=1)


class Pass_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=60)
    balance = models.FloatField(default=0)
    founded = models.DateTimeField('data founded')

    def __str__(self):
        return self.book_name

    def was_founded_recently(self):
        return self.founded >= timezone.now() - datetime.timedelta(days=1)


class Type_programe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=20)
    type_detail = models.CharField(max_length=500)

    def __str__(self):
        return self.type_name


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField()

    def __str__(self):
        return str(self.day)


class Month(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)

    def __str__(self):
        return self.month


class Year(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(default=2017) # change later

    def __str__(self):
        return str(self.year)


class Program(models.Model):
    pass_book = models.ForeignKey(Pass_book, on_delete=models.CASCADE)
    type_programe = models.ForeignKey(Type_programe, on_delete=models.CASCADE)
    day_published = models.ForeignKey(Day, on_delete=models.CASCADE)
    month_published = models.ForeignKey(Month, on_delete=models.CASCADE)
    year_published = models.ForeignKey(Year, on_delete=models.CASCADE)
    head_program = models.CharField(max_length=70)
    detail = models.CharField(max_length=500)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.head_program

