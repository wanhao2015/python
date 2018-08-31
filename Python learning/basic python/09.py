for i,value in enumerate(['A','B','C','D']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：    
def findMinAndMax(L):
    if L == []:
        return(None,None)
    min = max = L[0]
    for i,value in enumerate(L):
        if value < min:
            min = value
            min_i = i
        if value > max:
            max = value
            max_i = i
    return(min_i,min,max_i,max)
list1 = [2,0,3,9,5]
print(findMinAndMax(list1))  