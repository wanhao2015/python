# 把一个列表生成式的[]改成()，就创建了一个generator
g = (x*x for x in range(1,11))
for n in g:
    print(n)

# 如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator 
# 变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b     #等价下面注释语句
        # j = a 
        # a = b 
        # b = j + b
        n += 1
    return 'done'
for n in fib(10):
    print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
 
#杨辉三角，把每一行看做一个list，试写一个generator，不断输出下一行的list 
def triangles(max):
    n = 1
    L = [1]
    while n <= max:
        yield L
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
        n += 1
    return 'done'
for i in triangles(10):
    print(i)
    
# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，
# 不过可以通过iter()函数获得一个Iterator对象。



