from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']  # Adjust based on your model fields

    # You can also add custom validation if needed
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Add custom validation logic if necessary
        return title
