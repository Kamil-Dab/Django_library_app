from django.test import TestCase

from books.models import Book, BookSearcher, KeyValueBook


class BookTestModels(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            title='Harry Potter',
            author='J.K Rowling',
            publication_date=1997,
            number_of_pages=332,
            thumbnail_link='https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
            isbn_number='9780747532743',
            language='en')

    def test_first_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_first_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_first_publication_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('publication_date').verbose_name
        self.assertEqual(field_label, 'publication date')

    def test_first_number_of_pages_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('number_of_pages').verbose_name
        self.assertEqual(field_label, 'number of pages')

    def test_first_thumbnail_link_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('thumbnail_link').verbose_name
        self.assertEqual(field_label, 'thumbnail link')

    def test_first_isbn_number_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn_number').verbose_name
        self.assertEqual(field_label, 'isbn number')

    def test_first_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_first_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 400)

    def test_object_title(self):
        book = Book.objects.get()
        expected_object = f'{book.title}'
        self.assertEqual(str(book), expected_object)

    def test_output_author(self):
        book = Book.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 'J.K Rowling'
        self.assertEqual(output[0].author, expected_object)

    def test_output_publication_date(self):
        book = Book.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 1997
        self.assertEqual(output[0].publication_date, expected_object)

    def test_output_number_of_pages(self):
        book = Book.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 332
        self.assertEqual(output[0].number_of_pages, expected_object)

    def test_output_thumbnail_link(self):
        book = Book.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg'
        self.assertEqual(output[0].thumbnail_link, expected_object)

    def test_output_isbn_number(self):
        book = Book.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = '9780747532743'
        self.assertEqual(output[0].isbn_number, expected_object)


class BookSearcherTestModels(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        BookSearcher.objects.create(
            title='Harry Potter',
            author='J.K Rowling',
            to_date=1997,
            from_date=1995,
            language='en')

    def test_first_title_label(self):
        book = BookSearcher.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_first_author_label(self):
        book = BookSearcher.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_first_to_date_label(self):
        book = BookSearcher.objects.get(id=1)
        field_label = book._meta.get_field('to_date').verbose_name
        self.assertEqual(field_label, 'to date')

    def test_first_from_date_label(self):
        book = BookSearcher.objects.get(id=1)
        field_label = book._meta.get_field('from_date').verbose_name
        self.assertEqual(field_label, 'from date')

    def test_first_language_label(self):
        book = BookSearcher.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_first_name_max_length(self):
        book = BookSearcher.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_object_title(self):
        book = BookSearcher.objects.get()
        expected_object = f'{book.title}'
        self.assertEqual(str(book), expected_object)

    def test_output_author(self):
        book = BookSearcher.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 'J.K Rowling'
        self.assertEqual(output[0].author, expected_object)

    def test_output_to_date(self):
        book = BookSearcher.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 1997
        self.assertEqual(output[0].to_date, expected_object)

    def test_output_from_date(self):
        book = BookSearcher.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 1995
        self.assertEqual(output[0].from_date, expected_object)


class KeyValueBookTestModels(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        KeyValueBook.objects.create(key_word='Harry Potter')

    def test_first_key_word_label(self):
        book = KeyValueBook.objects.get(id=1)
        field_label = book._meta.get_field('key_word').verbose_name
        self.assertEqual(field_label, 'key word')

    def test_key_word_max_length(self):
        book = KeyValueBook.objects.get(id=1)
        max_length = book._meta.get_field('key_word').max_length
        self.assertEqual(max_length, 20)

    def test_output_key_word(self):
        book = KeyValueBook.objects.all()
        output = list()
        for item in book:
            output.append(item)
        expected_object = 'Harry Potter'
        self.assertEqual(output[0].key_word, expected_object)