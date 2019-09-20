## Dictionaries in python ##
############################

students ={} #empty dictionary
#dictionary with key/value pairs/items
#Ex: key = alice value= 25 item= alice:25
students = {"Alice":25,"Collin":30,"Elizabeth":28,"Angela":21,"Anne":21,"Alex":19} 

#key lookup
studnets[Alice] #25

# adding to dictionary
studnets ['Dan']=25

# modifying dictionary
students ['Alice'] =26

#remove from dictionary
del students['fred']

#list of keys
students.keys()

#dictionaries are iterable but no indexable
#to pick specific key out dict must turn dict into list

a = list(student.keys())
a[0] #Alice
a[1] #Collin

#list of values in dict
students.values()

#how to get dict to be indexable for values
list(students.values())

#you can use slicing w/ it
list(students.values()[2:]

#NOTE: dictionaries do NOT have an order unlike lists and tuples
