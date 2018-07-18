#循环语句,注意 for in 语句后面的冒号
datas = [1,2,3,4,6,5,7]
sum = 0
for data in datas:
    sum += data
print(sum)

#range(101)函数，可以生成一个大于等于0、小于101的整数序列，再通过list()函数可以转换为list
#计算 0+1+2+3+...+100
sum = 0
list1 = list(range(101))
for x in list1:
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -=2
print(sum)

#计算1*2*3*4*...*100  python里整型可以是任意大的数
mul = 1
n = 1
while n <= 100:
    mul *= n
    n += 1
print(mul)
