class Book:
  def __init__(self, title, author):
    self.author = author
    self.title = title
    self._is_checked_out = False

  def check_out_book(self):
    if not self._is_checked_out:
      self._is_checked_out = True
      return True

    else:
      return False

  def return_book(self):
    if self._is_checked_out:
      self._is_checked_out = False
      return True

    else:
      return False

  def availability(self):
    if not self._is_checked_out:
      return True
    else:
      return False
  
class Library:

  def __init__(self):
    self._books = []
  
  def add_book(self, book):
    self._books.append(book)

    return self._books

  
  def check_out_book(self, title):
    for book in self._books:
      if book.title == title:
        if book.check_out_book():
          #print(f"Checking out '{title}' book is successful ")
          pass
        else:
          #print(f"Note: The book '{title}' has already been checked out")
          pass
        return
    print(f'Error: The book {title} is not available in the library')

  def return_book(self, title):
    for book in self._books:
      if book.title == title:
        if book.return_book():
          #print(f"The '{book}' has been returned to the library")
          pass
        else:
          #print(f"Warning: The book '{title} was not checked out")
          pass
        return
    print(f"Error: This book '{title}', doesnt belong to your libary")

  def list_available_books(self):
    if len(self._books) > 0:
      for book in self._books:
        if book.availability():
          print(f"{book.title} by {book.author}")
    else:
      print('Note: No book available in the library')