from django.shortcuts import render, redirect
from .models import Book, BookSearcher
from .forms import BookForm, BookSearcherForm
from .serializers import BookSerializer
from django.contrib import messages
from rest_framework import generics


class BookPurchaseList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        to_date = self.request.query_params.get('to_date')
        from_date = self.request.query_params.get('from_date')
        language = self.request.query_params.get('language')
        if title is not None:
            queryset = queryset.filter(title=title)
        if author is not None:
            queryset = queryset.filter(author=author)
        if language is not None:
            queryset = queryset.filter(language=language)
        if to_date is not None:
            queryset = queryset.exclude(publication_date__gte=to_date)
        if from_date is not None:
            queryset = queryset.filter(publication_date__gte=from_date)
        return queryset


def home(request):
    return render(request, 'home.html', {})


def books(request):
    output = list()
    if request.method == 'POST':
        form = BookSearcherForm(request.POST or None)
        if form.is_valid():
            form.save()
            query_books = BookSearcher.objects.order_by('-id')[0]
            messages.success(request, "Book Has Been Filtered!")
            library = Book.objects.all()
            if len(library) == 0:
                query_books.delete()
                return render(request, 'books.html', {'output': 'Library is empty'})
            else:
                if query_books.title is not None:
                    library = library.filter(title=query_books.title)
                if query_books.author is not None:
                    library = library.filter(author=query_books.author)
                if query_books.to_date is not None:
                    library = library.exclude(publication_date__gte=query_books.to_date)
                if query_books.from_date is not None:
                    library = library.filter(publication_date__gte=query_books.from_date)
                if query_books.language is not None:
                    library = library.filter(language=query_books.language)
                query_books.delete()
                if len(library) == 0:
                    return render(request, 'books.html', {'output': 'Library is empty'})
                else:
                    for item in library:
                        output.append(item)
                    return render(request, 'books.html', {'library': library, 'output': output})
        else:
            messages.error(request, form.errors)
            return redirect('books')
    else:
        library = Book.objects.all()
        if len(library) == 0:
            return render(request, 'books.html', {'output': 'Library is empty'})
        else:
            for item in library:
                output.append(item)
        return render(request, 'books.html', {'library': library, 'output': output})


def add_books(request):
    output = list()
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Has Been Added!")
        else:
            messages.error(request, form.errors)
        return redirect('add_books')
    else:
        library = Book.objects.all()
        for item in library:
            output.append(item)
        return render(request, 'add_books.html', {'library': library, 'output': output})


def delete(request, book_id):
    item = Book.objects.get(pk=book_id)
    item.delete()
    messages.success(request, 'Book has been deleted')
    return redirect(add_books)


def edit(request, book_id):
    edit_item = Book.objects.get(pk=book_id)
    return render(request, 'edit.html', {'output': edit_item})


def update(request, book_id):
    update_item = Book.objects.get(pk=book_id)
    form = BookForm(request.POST, instance=update_item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Book updated successfully')
        return render(request, 'edit.html', {'output': update_item})
    else:
        messages.error(request, form.errors)
        return redirect('edit', book_id)


def import_books(request):
    import requests
    import json
    if request.method == 'POST':
        key_word = request.POST['key_word']
        if key_word == None or key_word == '':
            return redirect('import_books')
        else:
            key_word = request.POST['key_word']
            import_query = dict()
            api_request = requests.get(
                "https://www.googleapis.com/books/v1/volumes?q=" + key_word)
            try:
                api = json.loads(api_request.content)
            except Exception as e:
                api = "Error..."
            for book in api['items']:
                import_query['title'] = book['volumeInfo']['title']
                if 'authors' not in book['volumeInfo']:
                    import_query['author'] = None
                else:
                    import_query['author'] = book['volumeInfo']['authors'][0]
                if 'publishedDate' not in book['volumeInfo']:
                    import_query['publication_date'] = None
                else:
                    import_query['publication_date'] = int(book['volumeInfo']['publishedDate'][0:4])
                if 'pageCount' not in book['volumeInfo']:
                    import_query['number_of_pages'] = None
                else:
                    import_query['number_of_pages'] = book['volumeInfo']['pageCount']
                if 'imageLinks' not in book['volumeInfo']:
                    import_query['thumbnail_link'] = None
                else:
                    import_query['thumbnail_link'] = book['volumeInfo']['imageLinks']['thumbnail']
                for number in book['volumeInfo']['industryIdentifiers']:
                    if number['type'] == 'ISBN_10':
                        import_query['isbn_number'] = number['identifier']
                    elif number['type'] == 'ISBN_13':
                        import_query['isbn_number'] = number['identifier']
                    else:
                        import_query['isbn_number'] = None
                import_query['language'] = book['volumeInfo']['language']
                form = BookForm(import_query)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Book Has Been Added!")
                else:
                    messages.error(request, form.errors)
            return render(request, 'import_books.html', {'api': api})
    else:
        return render(request, 'import_books.html', {})
