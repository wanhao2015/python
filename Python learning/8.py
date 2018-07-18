# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(str):
    n = len(str)
    aa = 0
    bb = n
    for i in range(n):
        if str[i] == ' ':
            aa += 1
        else:
            break
    for j in range(1,n+1):
        if str[-j] == ' ':
            bb -= 1
        else:
            break
    str = str[aa:bb]
    return str

print(trim('  abc ac  '),len(trim('  abc ac  ')))

str1 = '  abc ac  '
str2 = '000adssf00'
print(str1.strip())
print(str2.strip('0'))
            