#!usr/bin/env python

class Person:
    def __init__(self, name="Vasya Puptin", job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s -> %s as %s]' % (self.name, self.pay, self.job)

"""
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "manager", pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
"""

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print person


if __name__ == '__main__':

    bob = Person('Bob Pypkin')
    sue = Person('Sue Jones', 'developer', 100000)
    print sue.job, sue.name, sue.pay
    sue.giveRaise(.10)
    print sue.pay
    print sue
    print bob
    tom = Manager('Tom Lower', 50000)
    tom.giveRaise(.10)
    print tom.lastName()
    print tom
    print "=" * 80

    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.50)
    development.showAll()
