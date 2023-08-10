def find_primes(start=3, end=None):
    pr_chisla = []
    while start <= end:
        k = 2
        sqrt = start ** 0.5
        while k <= sqrt:
            if start % k == 0:
                break
            k += 1
        else:
            pr_chisla.append(start)
        start += 1
    #  print(pr_chisla)
