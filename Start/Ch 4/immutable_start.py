# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0
    def somefunc(self, value):
        self.value2 = value

obj = ImmutableClass("Another string", 20) # can only be changed at creation
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.somefunc(1)
print(obj.value1, obj.value2)

# TODO: even functions within the class can't change anything
