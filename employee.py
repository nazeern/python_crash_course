class Employee():
    def __init__(self, first_name, last_name, salary):
        self.f_name = first_name
        self.l_name = last_name
        self.salary = salary
        self.attributes = []

    def give_raise(self, incr=5000):
        self.salary += incr

    def give_attribute(self, *attributes):
        for attribute in attributes:
            self.attributes.append(attribute)

a = Employee("Nitin", "Nazeer", 60000)
b = Employee("Nazeer", "Hussain", 0)        


