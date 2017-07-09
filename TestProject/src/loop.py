'''
Created on Jul 8, 2017

@author: iyyam
'''
for var in list(range(50)):
    print(var)
for a in list(range(10)):
        print(a)
        
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)
   
list = [1,2,3,4]
it = iter(list) # this builds an iterator object

for x in it:
    print(x)
print ("My name is %s and weight is %d kg!" % ('Zara', 21))

list = ['physics', 'chemistry', 1997, 2000]

print (list)
list[1]=2113213
del list[2]
print ("After deleting value at index 2 : ", list) 