from math import sqrt


def find_primes(start, end):
    lst = []
    if start > 1:
        for i in range(start, end+1):
            end2 = int(sqrt(i)) + 1
            for j in range(2,  end2):
                if j > end2:
                    lst.append(i)
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)
    print(lst)