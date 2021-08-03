from django.test import TestCase, Client
from django.urls import reverse

from books.models import Book, BookSearcher


class TestViews(TestCase):
    databases = '__all__'

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.books_url = reverse('books')
        self.add_books_url = reverse('add_books')
        self.delete_url = reverse('delete', args=[1])
        self.edit_url = reverse('edit', args=[1])
        self.update_url = reverse('update', args=[1])
        self.import_books_url = reverse('import_books')
        self.list_book_url = reverse('list_book')

        self.book_object1 = Book.objects.create(
            title='Harry Potter',
            author='J.K Rowling',
            publication_date=1997,
            number_of_pages=332,
            thumbnail_link='https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
            isbn_number='9780747532743',
            language='en')
        self.booksearch_object1 = BookSearcher.objects.create(
            title='Harry Potter',
            author='J.K Rowling',
            to_date=1997,
            from_date=1995,
            language='en')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_books_GET(self):
        response = self.client.get(self.books_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')

    def test_books_POST_correct_response(self):
        response = self.client.post(self.books_url, {
            'title': 'Harry Potter',
            'author': 'J.K Rowling',
            'to_date': 1997,
            'from_date': 1995,
            'language': 'en'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')

    def test_books_POST_no_data(self):
        response = self.client.post(self.books_url)

        self.assertEquals(response.status_code, 302)

    def test_add_books_GET(self):
        response = self.client.get(self.add_books_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_books.html')

    def test_add_books_POST_correct_response(self):
        response = self.client.post(self.add_books_url, {
            'title': 'Harry Potter',
            'author': 'J.K Rowling',
            'publication_date': 1997,
            'number_of_pages': 332,
            'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
            'isbn_number': '9780747532743',
            'language': 'en',
        })
        self.assertEquals(response.status_code, 302)

    def test_add_books_POST_no_data(self):
        response = self.client.post(self.add_books_url)

        self.assertEquals(response.status_code, 302)

    def test_import_books_GET(self):
        response = self.client.get(self.import_books_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'import_books.html')

    def test_import_books_POST_correct_response(self):
        response = self.client.post(self.import_books_url, {
            'key_word': 'Harry Potter'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'import_books.html')

    def test_import_books_POST_no_data(self):
        response = self.client.post(self.import_books_url, {
            'key_word': ''
        })

        self.assertEquals(response.status_code, 302)

    def test_delete_GET(self):
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 302)

    def test_edit_GET(self):
        response = self.client.get(self.edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 302)

    def test_update_POST(self):
        response = self.client.post(self.update_url,{
            'title': 'Harry Potter',
            'author': 'J.K Rowling',
            'publication_date': 1997,
            'number_of_pages': 332,
            'thumbnail_link': 'https://ecsmedia.pl/c/harry-potter-i-kamien-filozoficzny-tom-1-b-iext66938428.jpg',
            'isbn_number': '9780747532743',
            'language': 'en',
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_update_GET(self):
        response = self.client.get(self.list_book_url)
        print(self.book_object1.author)
        self.assertEquals(response.data[0]['title'], self.book_object1.title)
        self.assertEquals(response.status_code, 200)
