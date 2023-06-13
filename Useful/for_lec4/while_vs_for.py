#    012345
s = "ab1c2d3ef"
i = len(s) - 1
while i >= 0:
    if s[i].isdecimal():
        print(s[i])
    i -= 1

for x in s[::-1]:
    if x.isdecimal():
        print(x)

# x = s[0]
# x - не последний?
# x = x + 1