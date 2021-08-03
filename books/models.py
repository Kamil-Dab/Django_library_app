import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def validate_isbn_number_length(number):
    if not (len(str(number)) == 13 or len(str(number)) == 10):
        raise ValidationError('%(number)s must be 10 or 13 digits', params={'number': number})


def validate_isbn_control_number(number):
    if len(str(number)) == 13:
        sum_control = 10 - ((int(number[0]) + int(number[2]) + int(number[4]) + int(number[6]) + int(number[8]) + int(
            number[10]) + 3 * (int(number[1]) + int(number[3]) + int(number[5]) + int(number[7]) + int(number[9]) + int(number[11]))) % 10)
        if int(number[12]) != sum_control:
            raise ValidationError('ISBN-13 is invalid')
    if len(str(number)) == 10:
        sum_control = (int(number[0])*1 + int(number[1])*2 + int(number[2])*3 + int(number[3])*4 + int(number[4])*5 + int(
            number[5])*6 + int(number[6])*7 + int(number[7])*8 + int(number[8])*9) % 11
        if int(number[9]) != sum_control:
            raise ValidationError('ISBN-10 is invalid')


class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(blank=True, null=True, max_length=100)
    publication_date = models.PositiveIntegerField(blank=True, null=True,
                                                   validators=[MinValueValidator(1000), max_value_current_year])
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    thumbnail_link = models.URLField(blank=True, null=True, max_length=500)
    isbn_number = models.CharField(blank=True, null=True, max_length=13, validators=[validate_isbn_number_length, validate_isbn_control_number])
    language = models.CharField(blank=True, null=True, max_length=2,
                                help_text="Language should be written as two-letter abbreviation")

    def __str__(self):
        return self.title


class BookSearcher(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.PositiveIntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(1000), max_value_current_year])
    to_date = models.PositiveIntegerField(blank=True, null=True,
                                          validators=[MinValueValidator(1000), max_value_current_year])
    language = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.title


class KeyValueBook(models.Model):
    key_word = models.CharField(max_length=20)
