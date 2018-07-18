#input()返回的是字符串，需要通过float()转换成浮点型
temp1 = input('输入身高/m：')
temp2 = input('输入体重/kg：')
height = float(temp1)
weight = float(temp2)
bmi = weight/(height*height)
print('bmi =',bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <=25:
    print('正常')
elif bmi <=28:
    print('过重')
elif bmi <=32:
    print('肥胖')
else:
    print('严重肥胖')