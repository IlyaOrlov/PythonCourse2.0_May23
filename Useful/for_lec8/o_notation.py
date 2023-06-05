s = "abcde"
print(s[4])  # O(1)
s.find('e')
for i in s:  # O(N)
    if i == 'e':
        print(i)
        break

lst = ['a', 'b', 'c', 'd', 'e']
print(lst[4])  # O(N)
cnt = 0
for i in lst:  # O(N)
    if i == 'e':
        print(cnt, i)
        break
    cnt += 1

t = tuple(lst)
t = t + ('end',)
print(t)
