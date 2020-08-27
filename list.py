list1 = [4,56,["sun", "moon","earth"],('saturn', 'venus')]
list2 = ['c','c#','c++',]
list3 = ['python', 'Java', 'Javascript']


list2 = [] # empty list created
print('list1 = ',list1)
# accessing members of list
print('list1[2] :',list1[2])
print(('list1[2][0] = ',list1[2][0]))
print('list1[3][0] =',list1[3][0])
print('list1[-1] = ',list1[-1]) # for negative index access from right end
# updating list members
list1.append('Jupiter')
print(' updated list1 : ', list1)
# detele operations
del list1[2]
print('After deleting element at index 2, list1 =', list1)