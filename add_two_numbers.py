#https://leetcode.com/problems/add-two-numbers/description/

list1 = [2,4,3]
list2 = [5,6,4]

ls1 = len(list1)
ls2 = len(list2)

#padding 0 to high bit
if(ls1>ls2): 
    diff = ls1 - ls2
    i = 0
    while (i<diff):
        list2.append(0)
        i+=1

if(ls2>ls1): 
    diff = ls2 - ls1
    i = 0
    while (i<diff):
        list1.append(0)
        i+=1

size = len(list1)
flag = 0
list3 = [0]*size
for i in range(0,size):
    bit = list1[i] + list2[i] + flag
    if(bit > 9):
        flag = 1
        bit %= 10
    else:
        flag = 0
    list3[i] = bit

print list3