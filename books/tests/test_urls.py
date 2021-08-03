from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import home, books, add_books, delete, edit, update, import_books, BookPurchaseList


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_books_url_is_resolves(self):
        url = reverse('books')
        self.assertEquals(resolve(url).func, books)

    def test_add_books_url_is_resolves(self):
        url = reverse('add_books')
        self.assertEquals(resolve(url).func, add_books)

    def test_import_books_url_is_resolves(self):
        url = reverse('import_books')
        self.assertEquals(resolve(url).func, import_books)

    def test_list_book_url_is_resolves(self):
        url = reverse('list_book')
        self.assertEquals(resolve(url).func.view_class, BookPurchaseList)

    def test_delete_url_is_resolves(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, delete)

    def test_update_url_is_resolves(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func, update)

    def test_edit_url_is_resolves(self):
        url = reverse('edit', args=[1])
        self.assertEquals(resolve(url).func, edit)
