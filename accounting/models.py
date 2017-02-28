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

    def set_balance(self, value):
        self.balance = value


class List_type(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=20)
    type_detail = models.CharField(max_length=500)
    type_for = models.CharField(max_length=20, default="income")

    def __str__(self):
        return self.type_name


class List(models.Model):
    pass_book = models.ForeignKey(Pass_book, on_delete=models.CASCADE)
    list_type = models.ForeignKey(List_type, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=70)
    detail = models.CharField(max_length=500)
    value = models.FloatField(default=0)
    date = models.DateField(default= datetime.date.today)

    def __str__(self):
        return self.list_name

    def set_value(self, val):
        self.value = val

    def get_date(self):
        if(self.date.month >9):
            month = str(self.date.month)
        else:
            month = "0" + str(self.date.month)
        if(self.date.day >9):
            day = str(self.date.day)
        else:
            day = "0" + str(self.date.day)
        year = str(self.date.year)
        date = year + "-" + month + "-" + day
        return date

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day


class Imported_csv(models.Model):
    description = models.CharField(max_length=255, blank=True)
    csv_file = models.FileField(upload_to='./accounting/media/imported_csv/')
    pass_book = models.ForeignKey(Pass_book, on_delete=models.CASCADE, default='1')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def get_csv_file(self):
        return str(self.csv_file)
