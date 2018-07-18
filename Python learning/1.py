print('hello world')
print('''line1,\n
line2
line3''')
a = 123
print(a)
b = 'ADF'
print(b)
c = 3
d = 2
e = a / 3
f = a // d 
print('%f %d' %(e,f))

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.1f%%',r)

classmate = ['aa','bb','cc']
len1 = len(classmate)
print(classmate[-1],len1)
classmate.append('dd')
print(classmate[-1],len(classmate))
classmate.insert(3,55)
print(classmate[3],len(classmate))
classmate.pop(3)
print(classmate[3],len(classmate))

#tuple类型指向的元素不能变，
list1 = ['a','b']
tup = (1,2,3,list1,4)
print(tup)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])


    
