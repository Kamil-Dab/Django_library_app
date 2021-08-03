from django import forms
from django.core.exceptions import ValidationError

from .models import Book, BookSearcher, KeyValueBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publication_date",
            "number_of_pages",
            "thumbnail_link",
            "isbn_number",
            "language",
        ]


class BookSearcherForm(forms.ModelForm):
    class Meta:
        model = BookSearcher
        fields = [
            "title",
            "author",
            "from_date",
            "to_date",
            "language",
        ]

    def clean(self):
        cd = self.cleaned_data

        from_date = cd.get("from_date")
        to_date = cd.get("to_date")
        if from_date is not None and to_date is not None:
            if from_date > to_date:
                raise ValidationError("Start date should be earlier than end date")
        return cd


class KeyValueBookForm(forms.ModelForm):
    class Meta:
        model = KeyValueBook
        fields = {
            'key_word'
        }
