# Example script

import os
import sys
import django

# # Add your project path to sys.path
# sys.path.append('/path/to/your/project')  # Replace with the actual path to your project
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Replace with your project's settings module

# Configure Django
django.setup()

from myapp.models import Book
from myapp.serializers import BookSerializer

data = {
    'title': 'IF THEN', 
    'author': 'Jill Leopore', 
    'publication_year': 2020, 
    'isbn': '978152936172'
}

serializer = BookSerializer(data=data)

if serializer.is_valid():
    book_instance = serializer.save()
    print("Book instance saved successfully.")
    
    # to view the attributes of the saved Book instance
    print(f"Title: {book_instance.title}")
    print(f"Author: {book_instance.author}")
    print(f"Publication Year: {book_instance.publication_year}")
    print(f"ISBN: {book_instance.isbn}")
    
else:
    print("Error creating book instance. Validation errors:")
    print(serializer.errors)
