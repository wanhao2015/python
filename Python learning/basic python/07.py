def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))

def move(n, a, b, c): 
    if n == 1:   # 如果a只有1盘子
        global aa
        aa += 1
        print(a, '-->', c)   # 直接把盘子从a移到c
    else:   # 如果a有n个盘子(n > 1)，那么分三步
        move(n-1, a, c, b)   # 先把上面n-1个盘子，借助c，从a移到b
        move(1, a, b, c)   # 再把最下面的1个盘子，借助b，从a移到c
        move(n-1, b, a, c)   # 最后把n-1个盘子，借助a，从b移到c
aa = 0
move(4,'A','B','C')  # 测试
print(aa)