import abc
import random
import unittest


class Visitable:

    def accept(self, visitor):
        visitor.visit(self)


class CompositeVisitable(Visitable):

    def __init__(self, iterable):
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)


class AbsctractVisitor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def visit(self, element):
        raise NotImplementedError("A Visitor need to define a visit method")

class Light(Visitable):

    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.status != -1

    def boot_up(self):
        self.status = 0

class LightStatusUpdateVisitor(AbsctractVisitor):

    def __init__(self, person_1_home, person_2_home):
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = 1
            else:
                element.status = 0
        elif self.person_2_home:
            element.status = 1
        else:
            element.status = 0


class Thermostat(Visitable):

    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        temp_range = [x for x in range(-10, 31)]
        temp_range.append(None)
        return random.choice(temp_range)

    def is_online(self):
        return self.status is not None

    def boot_up(self):
        pass


class ThermostStatusUpdateVisitor(AbsctractVisitor):

    def __init__(self, person_1_home, person_2_home):
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        pass


