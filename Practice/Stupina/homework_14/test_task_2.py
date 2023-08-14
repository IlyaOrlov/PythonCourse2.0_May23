import unittest
from task_2 import Money, IncorrectDataInput


class MyTest(unittest.TestCase):
    ob1 = Money(10, 20)
    ob2 = Money(10, 0)
    ob3 = Money(5, 30)

    def test_money_eq(self):
        self.assertEquals(str(self.ob1), '10,20')

    def test_sub(self):
        self.assertEquals(str(self.ob1-self.ob2), '0,2')

    def test_add(self):
        self.assertEquals(str(self.ob1 + self.ob3), '15,5')

    def test_lt(self):
        self.assertTrue(self.ob1 > self.ob3)

    def test_eq(self):
        self.assertFalse(self.ob1 == self.ob3)

    def test_le(self):
        self.assertTrue(self.ob2 <= self.ob1)

    def test_er(self):
       with self.assertRaises(IncorrectDataInput):
            Money(-5, 30)

    def test_er1(self):
       with self.assertRaises(IncorrectDataInput):
            Money(5, 306)





