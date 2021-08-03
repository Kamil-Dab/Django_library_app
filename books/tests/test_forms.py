from django.test import TestCase

from books.forms import BookForm, BookSearcherForm, KeyValueBookForm


class BookFormTest(TestCase):
    def test_title_form_date_field_label(self):
        form = BookForm()
        self.assertTrue(form.fields['title'].label is None or form.fields['title'].label == 'Title')

    def test_None_value_for_all(self):
        form = BookForm(
            data={'title': None, 'author': None, 'publication_date': None, 'number_of_pages': None,
                  'thumbnail_link': None, 'isbn_number': None, 'language': None})
        self.assertFalse(form.is_valid())

    def test_correct_value_for_all(self):
        form = BookForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'publication_date': 1997, 'number_of_pages': 332,
                  'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
                  'isbn_number': '9780747532743', 'language': 'en'})
        self.assertTrue(form.is_valid())

    def test_publication_date_too_big(self):
        form = BookForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'publication_date': 19970, 'number_of_pages': 332,
                  'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
                  'isbn_number': '9780747532743', 'language': 'en'})
        self.assertFalse(form.is_valid())

    def test_number_of_pages_is_negative(self):
        form = BookForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'publication_date': 1997, 'number_of_pages': -332,
                  'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
                  'isbn_number': '9780747532743', 'language': 'en'})
        self.assertFalse(form.is_valid())

    def test_invalid_isbn_number(self):
        form = BookForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'publication_date': 1997, 'number_of_pages': 332,
                  'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
                  'isbn_number': '9788363944546', 'language': 'en'})
        self.assertFalse(form.is_valid())

    def test_invalid_language(self):
        form = BookForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'publication_date': 1997, 'number_of_pages': 332,
                  'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
                  'isbn_number': '9788363944546', 'language': 'English'})
        self.assertFalse(form.is_valid())


class BookSearcherFormTest(TestCase):
    def test_title_form_date_field_label(self):
        form = BookSearcherForm()
        self.assertTrue(form.fields['title'].label is None or form.fields['title'].label == 'Title')

    def test_None_value_for_all(self):
        form = BookSearcherForm(data={'title': None, 'author': None, 'to_date': None, 'from_date': None,'language': None})
        self.assertTrue(form.is_valid())

    def test_correct_value_for_all(self):
        form = BookSearcherForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'to_date': 2000, 'from_date': 1997,  'language': 'en'})
        self.assertTrue(form.is_valid())

    def test_wronge_date_range(self):
        form = BookSearcherForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'to_date': 1997, 'from_date': 2000,  'language': 'en'})
        self.assertFalse(form.is_valid())

    def test_invalid_language(self):
        form = BookSearcherForm(
            data={'title': 'Harry Potter', 'author': 'J.K Rowling', 'to_date': 1997, 'from_date': 2000,  'language': 'English'})
        self.assertFalse(form.is_valid())


class KeyValueBookFormTest(TestCase):
    def test_None_value_for_all(self):
        form = KeyValueBookForm(data={'key_word': None})
        self.assertFalse(form.is_valid())

    def test_correct_value_for_all(self):
        form = KeyValueBookForm(data={'key_word': 'Harry Potter'})
        self.assertTrue(form.is_valid())

    def test_too_long_string(self):
        form = KeyValueBookForm(data={'key_word': 'Harrysadasdasdasdadssadasdasda2r1212rfrgerwergerafaPotter'})
        self.assertFalse(form.is_valid())