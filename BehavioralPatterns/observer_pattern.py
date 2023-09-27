"""
The Observer Pattern is a behavioral design pattern that defines a one-to-many
dependency between objects, so that when one object (the subject or observable)
changes its state, all its dependents (observers) are notified and updated
automatically. This pattern is used to establish a loosely coupled relationship
between objects, allowing them to communicate with each other without having
to know too much about each other's internal workings.

Key components of the Observer Pattern:

Subject (Observable): This is the object that maintains a list of observers and
provides methods to attach, detach, and notify observers of changes in its state.
The subject is the object being observed.

Observer: This is an interface or an abstract class that defines the update method.
Concrete observer classes implement this method to respond to changes in the
subject's state.

Concrete Subject: This is a concrete implementation of the subject interface.
It keeps track of its observers and notifies them when its state changes.

Concrete Observer: These are concrete implementations of the observer interface.
They register with a subject to receive updates and define how they respond
to changes in the subject's state.
"""

from collections import UserList


class Observer:
    """ Abstract class for Observer object """
    def __init__(self, title):
        self.title = title

    def update(self, message):
        ...


class Observable:
    """ any class inherits from this class will become observable """
    def __init__(self):
        self._observers = []

    @property
    def observers(self):
        return self._observers

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class MyListsObserver(Observer):
    """ Concrete class of Observer, Implements update method """

    def update(self, message):
        print(f"from {self.title} list has changed.", message)

class UpdateGUIListObserver(Observer):
    """ Concrete class of Observer, Implements update method """

    def update(self, message):
        print(f"My list updated. now update list in GUI", message)
        print(self)


class MyList(UserList, Observable):
    """ a personalized list sequence """

    def __init__(self, *iterable):
        super().__init__(iterable)
        Observable.__init__(self)

    def append(self, item) -> None:
        super().append(item)

        # notify observers
        message = f"{item} added to list"
        self.notify(message)

    def __setitem__(self, key, value) -> None:
        super().__setitem__(key, value)

        # notify observers
        message = f"item[{key}] changed to {value}"
        self.notify(message)

observer1 = MyListsObserver("Observer1")
observer2 = UpdateGUIListObserver("Observer2")

list1 = MyList(1,2,3,4,5)
list1.attach(observer1)
list1.attach(observer2)
list1.append(23)

list2 = MyList(*"helloWorld!")
list2.attach(observer1)
list2.attach(observer2)
list2[5:] = "John!"

# print(tlist)
