s = 'My card CVV is 111'
key = 555

lst = list(s)
print(lst)
lst = [ord(x) for x in lst]
print(lst)
code_lst = [x ^ key for x in lst]
print(code_lst)
code_s = '.'.join([str(x) for x in code_lst])
print(code_s)
with open('myfile', 'w') as f:
    f.write(code_s)

