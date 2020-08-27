str1 = "gyan matrix"
for i in str1:
    print(i)

print('-------------------------------------------')
print('String Reverse')
str2 = ""
for i in str1:
    str2 = i + str2
print(str2)
print('Accessing sub string')
str3 = str1[5:15]
print(str3)
print('Strings can also be accessed with -ve indexing')
print(str1[-13:-3])