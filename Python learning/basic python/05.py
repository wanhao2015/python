# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

#input()函数返回的值是 str 类型，需要转换

import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    x = x*x
    if x < 0:
        return -x
    else:
        return x
print(my_abs(-5))

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

def equation(a,b,c):
    if not (isinstance(a,(int,float)) & isinstance(c,(int,float)) & isinstance(b,(int,float))):
        raise TypeError('bad operand type')
    if a == 0:
        print('重新输入a值')
        return
    k = (b*b-4*a*c)
    if k == 0:
        print('只有一个根：')
        x = -b/(2*a)
        return x
    elif k > 0:
        print('有两个根：')
        x1 = ((-b) + math.sqrt(k))/(2*a)
        x2 = ((-b) - math.sqrt(k))/(2*a)
        return x1,x2
    else:
        print('没有实数根：')
        return

a = int(input())
b = int(input())
c = int(input())
data = equation(a,b,c)
print(data)
        
        
        
        
        
