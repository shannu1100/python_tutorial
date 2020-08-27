list1 = [4, 56, ["sun", "moon", "earth"], ('saturn', 'venus')]
list2 = ['c', 'c#', 'c++', ]
list3 = ['python', 'Java', 'Javascript']
# append()
list1.append(list2)
print('list1 after updation =',list1)
# append() takes the parameter as single element
list1.append('a')
print('list1 after updation =', list1)
# extend()
list2.extend('mongodb')
print('list2 after updation = ', list2)
list1[2].extend('Dollar')
print('list1[2] = ',list1[2])
# insert(index, element)
list3.insert(2,'html')
print('list3 =',list3)
list3.insert(2, ['mysql', 'noSql', 'mongoDb'])
print('updated list3 =',list3)