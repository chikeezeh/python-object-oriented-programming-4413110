# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance

class Publication:
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period) -> None:
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period) -> None:
        super().__init__(title, price, period, publisher)

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(n1.title)
print(n1.period)
print(n1.price)
print(n1.publisher)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
print(isinstance(n1, Newspaper))