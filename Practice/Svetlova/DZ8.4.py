from itertools import chain, combinations, filterfalse, product

def merge_arrays(arr1, arr2, arr3):
    merged_array = list(chain(arr1, arr2, arr3))
    return merged_array

def filter_strings(strings):
    filtered_strings = list(filterfalse(lambda s: len(s) < 5, strings))
    return filtered_strings

def generate_combinations(length):
    password = 'password'
    comb = list(combinations(password, length))
    return comb

# Пример использования
array1 = [1, 2, 3]
array2 = [4, 5]
array3 = [6, 7]
merged = merge_arrays(array1, array2, array3)
print("Merged array:", merged)

strings = ['hello', 'i', 'write', 'cool', 'code']
filtered = filter_strings(strings)
print("Filtered strings:", filtered)

combinations_list = generate_combinations(4)
print("Combinations:")
for combination in combinations_list:
    print(combination)