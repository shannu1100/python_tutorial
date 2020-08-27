'''#x = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,11):
    if i != 3:
        if i != 4:
          print (i)

'''
"""
v = ('shanmugam')
for i in v :
    if i != 'a':
     print (i) 
 """

list = []
while True:
    print("enter the name: ")
    num = (input())

    if num in list:
        print("already  that existed")
        break
    else:
        print(num)
        list.append(num)




