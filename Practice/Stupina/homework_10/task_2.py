from multiprocessing import Pool
import os


def my_sum(*args):
    print(f'This process {os.getpid()} ')
    if args:
        s = args[0]
        for i in args[1:]:
            s += i
    else:
        s = None
    return s


if __name__ == '__main__':
    lst_1, lst_2, lst_3 = [], [], []

    for i in range(1000000):
        lst_1.append(i)
        lst_2.append(i**2)
        lst_3.append(chr(i+100))

    par = [range(10000000), (lst_1, lst_2, lst_3), ('abc', 'defgh', 'iklmnopqrst')]

    count_p = len(par)
    pool = Pool(processes=count_p)
    res = pool.starmap(my_sum, par)
