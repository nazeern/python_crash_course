from employee import Employee
import unittest

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Nitin", "Nazeer", 60000)

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 65000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(60000)
        self.assertEqual(self.employee1.salary, 120000)

    def test_give_single_attribute(self):
        self.employee1.give_attribute("kind")
        self.assertIn("kind", self.employee1.attributes)

    def test_give_multiple_attributes(self):
        self.employee1.give_attribute("kind", "hard-working", "ambitious")
        for attribute in self.employee1.attributes:
            self.assertIn(attribute, self.employee1.attributes)

unittest.main()
