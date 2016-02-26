import datetime
import time


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print self.data


class SecondClass(FirstClass):
    def display(self):
        print "Current value = ", self.data


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[Third class: %s]' % self.data

    def mul(self, other):
        self.data *= other

x = FirstClass()
x.setdata(datetime.datetime.now())
x.display()
y = FirstClass()
y.setdata(datetime.datetime.now())
y.display()
c = SecondClass()
c.setdata(24)
c.display()
print dir(c)

a = ThirdClass("abc")
a.display()
print(a)
b = a + "zcd"
b.display()
print(b)

a.mul(20)
print a
