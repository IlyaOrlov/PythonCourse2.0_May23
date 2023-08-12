class MyException(Exception):
    pass


def num_to_roman(n):
    if not isinstance(n, int) or n < 1 or n > 5000:
        raise MyException('NonValidInput')

    r = {1000: 'M', 900: 'CM', 800: 'DCCC', 700: 'DCC', 600: 'DC', 500: 'D', 400: 'CD', 300: 'CCC', 200: 'CC', 100: 'C',
         90: 'XC', 80: 'LXXX', 70: 'LXX', 60: 'LX', 50: 'L', 40: 'XL', 30: 'XXX', 20: 'XX', 10: 'X',
         9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI', 5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I'}
    s = ''
    d = [1000, 100, 10, 1]
    d = d[(4-len(str(n))):]
    for i in d:
        if i == 1:
            s += r[n]
        else:
            res = n // i
            if res >= 1:
                if i == 1000:
                    s += r[i]*res
                else:
                    s += r[i*res]
                n -= res * i
    return s
