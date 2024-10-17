# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "A secret attribute"
    def getprice(self):
        if hasattr(self,"_discount"):
            return (100 - self._discount)*(self.price) / 100
        return self.price
        # TODO: add properties

    # TODO: create instance methods
    def setdiscount(self,amount):
        self._discount = amount
    def __repr__(self) -> str:
        return self.__secret

# TODO: create some book instances
b1 = Book("War and Peace","LT", 1225, 225)
b2 = Book("The Catcher in the Rye","JD Salinger", 234, 29.35)

# TODO: print the price of book1
print(b1.getprice())
print(b2.getprice())
b1.setdiscount(25)
print(b1.getprice())
print(b1)


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
# try updating the discount
