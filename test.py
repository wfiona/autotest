# -*- coding:utf-8 -*-

'''
s1 = 0
k = int(input("please input num："))
for j in range(1,7):
    s = 1
    for i in range(1,k+1):
        print (f"循环第{i}，结果为s = {s}*{j}")
        s = s*j
    print (f"{j}的{k}次幂，结果为{s}")
    
    print (f"s1 = {s1} + {s}")  
    s1 = s1 + s
    print (s1) 
'''

'''
#只考虑了k为0及正整数的情况
def mihanshu(k,j):
    s = 1
    for i in range(1,k+1):
        #print (f"循环第{i}，结果为s = {s}*{j}")
        s = s*j
    #print (f"{j}的{k}次幂，结果为{s}")
    return s

s1 = 0
k = int(input("please input num："))
for j in range(1,7):
    s1 = s1 + mihanshu(k, j)
print (s1)   
'''

'''
def mihanshu(k,j):
    s = 1
    if k >=0:
        for i in range(1,k+1):
            #print (f"循环第{i}，结果为s = {s}*{j}")
            s = s*j
            #print (f"{j}的{k}次幂，结果为{s}")
        #print (s)
        return s
    
    else:
        k = -k
        for i in range(1,k+1):
            #print (f"循环第{i}，结果为s ={s}*(1.0/{j})")
            s = s*(1.0/j)
            #print (f"{j}的{k}次幂，结果为{s}")
        #print (round(s,5))
        return round(s,5)

s1 = 0
k = int(input("please input num："))
for j in range(1,7):
    s1 = s1 + mihanshu(k, j)
print (s1)


'''
list = [[77,36,63,89],[96,21,82,87],[54,78,56,75],[92,67,78,73]]


small_list = []
for i in range(0,4):
    for j in range(0,3):
        if list[i][j] < list[i][j+1]:
            list[i][j+1],list[i][j] = list[i][j],list[i][j+1]
            j = j+1
        #small_list = list[i][j]
        #print (small_list) 
    small_list.append(int(list[i][j]))
    #print (list[i])
    i = i+1
    
#print (samll_list)     
for x in range(0,3):
    #print (type(samll_list[x]))
    #print (type(samll_list[x+1]))
    if small_list[x] < small_list[x+1]:
        small_list[x],small_list[x+1] = small_list[x+1],small_list[x]
        x = x+1
    #print(samll_list)
print(small_list[x])
 

  
    

   














