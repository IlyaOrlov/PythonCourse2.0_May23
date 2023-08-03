import multiprocessing as mp
import math
import os


def file_handler(fname_lst):
    lst = []
    for fname in fname_lst:
        with open(fname) as f:
            s = f.read().strip()
            if (i := int(s)) % 10 == 0:
                lst.append(i)
    print(lst)


if __name__ == "__main__":
    fname_lst = []
    for fname in os.listdir('.'):
        if fname.startswith("file"):
            fname_lst.append(fname)


    num_of_proc = os.cpu_count() - 1
    process_lst = []
    num_per_proc = math.ceil(len(fname_lst) / num_of_proc)
    start = 0
    stop = num_per_proc
    for i in range(num_of_proc):
        slice = fname_lst[start:stop]
        start = stop
        stop += num_per_proc
        p = mp.Process(target=file_handler, args=(slice,))
        p.start()
        process_lst.append(p)

    for p in process_lst:
        p.join()
