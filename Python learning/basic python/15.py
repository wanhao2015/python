from io import StringIO

# f = StringIO("Hi!\n  hello world!\n Bob")
# while True:
#     s = f.readline()
#     if s == "":
#         break
#     print(s.strip())

# 当使用StringIO()去初始化的时候，其指针是指向0的位置；而如果是用write的方法的时候，其指针则是会移动到后面的
sio = StringIO('abc')   #这里是初始化，指针指向0
print(sio.getvalue())
sio = StringIO('def')   #这里是再次初始化，指针仍然指向0 #def覆盖原值abc
print(sio.getvalue())
sio.write('ghi')       #这里要注意了，虽然是追加，但是由于指针仍然是0，所以实际上仍然会覆盖掉原值
print(sio.getvalue())
sio.write('ghi')       #上面第一次追加以后，指针就向后移动，所以此处才真正起到追加的效果
print(sio.getvalue())



