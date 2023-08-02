class MyError(Exception):
    pass

class MyFun:
    __roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                       'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                       'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def to_roman(self, number):
        roman = ''
        if not isinstance(number, int) or number not in range(1, 5001):
            raise MyError('NonValidInput')
        for i, value in self.__roman_numbers.items():
            while number >= value:
                roman += i
                number -= value
        return roman


m1 = MyFun()
