def find_dup(arr):  # O(n^2)
    lst1 = list()
    for i in arr:  # O(n)
        if i in lst1:  # O(n)
            return i
        else:
            lst1.append(i)
    return None


def find_dup_opt(arr):  # O(n)
    s1 = set()
    for i in arr:  # O(n)
        if i in s1:  # O(1)
            return i
        else:
            s1.add(i)
    return None


lst = [2, 1, 3, 1]
f = find_dup(lst)


# Flake8