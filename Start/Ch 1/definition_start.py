# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self, name) -> None:
     self.name = name

  def __repr__(self) -> str:
      return f"This is a Book class with name = {self.name}"

# TODO: create instances of the class
book1 = Book("LOTR")

# TODO: print the class and property
print(book1)