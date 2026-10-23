from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# Read: Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html',
                  {'books': books})


# Create: Add a book
def book_create(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    return render(request, 'books/book_form.html', {
        'form': form,
        'heading': 'Add Book'
    })


# Update: Edit a book
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'books/book_form.html',
                  {'form': form, 'heading': 'Edit Book'})


# Delete: Remove a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/book_confirm_delete.html',
                  {'book': book})