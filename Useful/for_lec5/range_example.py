#    012345
s = "aВbcАdeKf"  # BAK
s1 = ""

# В этом примере лучше без range, т.к. индексы отдельных символов не нужны. Нужны только сами символы.
for i in s:
    if i.isupper():
        s1 += i
print(s1)

# for idx in range(len(s)):
#     if s[idx].isupper():
#         s1 += s[idx]
# print(s1)


