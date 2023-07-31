class MyError(Exception):
    def __init__(self, text):
        self.txt = text

class MyFun:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        roman = ''
        if not isinstance(self.number, int) and self.number not in range(1, 5001):
            raise MyError('NonValidInput')
        for i, value in roman_numbers.items():
            while self.number >= value:
                roman += i
                self.number -= value
        return roman


roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
m1 = MyFun(566)
print(m1.to_roman())
