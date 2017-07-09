'''
Created on Jul 8, 2017

@author: iyyam
'''


List = ['peru','sankar','Raj','Nathan','Nithin','Aruna']

print(List) #print List
print(List[0]) #First value
print(List[0:3]) #Range value
print(List[3:]) #Range value
a = 'peru'
if ( a in List ):
   print (a," - a is available in the given list")
#read-only lists
tuple = (1,2,4,6)
tuple2 = (11,12,41,16)

print(tuple)
print(tuple[2:4])
print(tuple*2)
print(tuple+tuple2)

#Dictionary
dict = {'key1':'value1','key2':'value2'}

print(dict)
print (dict['key1'])       # Prints value for 'one' key
print (dict.keys())   # Prints all the keys
print (dict.values()) # Prints all the values