from multiprocessing import Pool
import os


lst = []


def my_sum(*args):
    lst.append(args)
    print(f'This process {os.getpid()} processed values {lst}')

    if args:
        s = args[0]
        for i in args[1:]:
            s += i
    else:
        s = None

    return s


if __name__ == '__main__':

    lst_1 = []
    lst_2 = []
    lst_3 = []

    par_0 = [i for i in range(100)]

    for i in range(20):
        lst_1.append(i)
        lst_2.append(i**2)
        lst_3.append(chr(i+100))

    par = [tuple(par_0), (lst_1, lst_2, lst_3), ('abc', 'defgh','iklmnopqrst')]

    count_p = len(par)
    pool = Pool(processes=count_p)
    res = pool.starmap(my_sum, par)
    print(res)
