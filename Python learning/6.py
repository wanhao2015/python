# 位置参数
# 默认参数     默认参数必须指向不变对象  
# 可变参数
# 关键字参数
# 命名关键字参数
# 参数组合

import math

def power(x,n=2):
    s = 1
    while n > 0:
        s = s*n
        n -= 1
    return s
print(power(5))
print(power(5,4))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n 
    return sum
print(calc(1,2,3,4))
print(calc())
nums = [1,2,3]
print(calc(*nums))    #*nums表示把nums这个list的所有元素作为可变参数传进去

#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。只接收city和job作为关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job) 
person1('Jack',24,city='shanghai',job='Engineer')    

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person2(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city':'Beijing','job':'Engineer'}
person2('Jack',24,**extra)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
  
  
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

