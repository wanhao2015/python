import os

# 列表生成式,
L = [x*x for x in range(1,11) if x%2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出文件所在目录下的所有文件列表
L = [d for d in os.listdir('.')]
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

#把一个列表中是字符串的元素变成小写字母字符串，其他的不变
def strlower(L):
    if L == []:
        return
    LL = []
    for str1 in L:
        if isinstance(str1,str):
            str1 = str1.lower()
        LL.append(str1)
    return LL
L1 = ['HELLO', 'World', 18, 'Apple', None]
L2 = print(strlower(L1))

L1 = ['HELLO', 'World', 18, 'Apple', None]
L2 = [str1.lower() for str1 in L1 if isinstance(str1,str)]
print(L2)



