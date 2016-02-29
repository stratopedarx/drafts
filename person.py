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
        return '[Person: %s -> %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)



if __name__ == '__main__':

    bob = Person('Bob Pypkin')
    sue = Person('Sue Jones', 'developer', 100000)
    print sue.job, sue.name, sue.pay
    sue.giveRaise(.10)
    print sue.pay
    print sue
    print bob
