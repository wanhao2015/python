# dict 字典 即C++ map (key-value) 具有极快的查找速度
dict1 = {'Michael':95,'Bob':80,'Tracy':75}
print(dict1['Bob'])

if 'Bob' in dict1:
    dict1.pop('Bob')
print(dict1)

#set 也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1,2,3])
print(s)
s.add(4)
s.add('a')
s.add(4)
print(s)
s.remove(4)
print(s)


