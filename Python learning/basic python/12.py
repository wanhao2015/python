from functools import reduce
import re
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def fun_1(name):
    return name[0].upper()+name[1:].lower()
list_1 = ['adam', 'LISA', 'barT']
print(list(map(fun_1,list_1)))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积:
def prod(list):
    def fun_2(x,y):
        return x*y
    return  reduce(fun_2,list)
# list_2 = [1,3,5,7,9]
# print(prod(list_2))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(str_1):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fun_3(x,y):
        return x*10+y
    def char2num(ch):
        return DIGITS[ch]
    if re.match(r'\d*\.\d*',str_1):
        str_2 = re.split(r'\.',str_1)
        data_1 = str_2[0]
        data_2 = str_2[1]
        data1 = reduce(fun_3,map(char2num,data_1))
        data2 = reduce(fun_3,map(char2num,data_2))
        data2 = data2/pow(10,len(data_2))
        return data1 + data2
str_1 = '10.00'
print(str2float(str_1))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(num):
    str1 = str(num)
    return str1 == str1[::-1]
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print(L2)
print(L3)

