## Dictionaries in python ##
############################

#NOTE: dictionaries do NOT have an order unlike lists and tuples

#students ={} #empty dictionary
#dictionary with key/value pairs/items
#Ex: key = alice value= 25 item= alice:25
#students = {"Alice":25,"Collin":30,"Elizabeth":28,"Angela":21,"Anne":21,"Alex":19} 

#key lookup
#studnets[Alice] #25

# adding to dictionary
#studnets ['Dan']=25

# modifying dictionary
#students ['Alice'] =26

#remove from dictionary
#del students['fred']

#list of keys
#students.keys()

#dictionaries are iterable but no indexable
#to pick specific key out dict must turn dict into list

#a = list(student.keys())
#a[0] #Alice
#a[1] #Collin

#list of values in dict
#students.values()

#how to get dict to be indexable for values
#list(students.values())

#you can use slicing w/ it
#list(students.values()[2:]

#list items in dict
#student.items()

################################################
## Allowing each key to store multiple values!
################################################

students = {"Alice":{"id":"ID00","age":25,"grade":"B+"},
            "Collin":{"id":"ID01","age":30,"grade":"SSS"},
            "Elizabeth":{"id":"ID02","age":28,"grade":"A"},
            "Angela":{"id":"ID03","age":22,"grade":"S"},
            "Anne":{"id":"ID04","age":21,"grade":"B"},
            "Alex":{"id":"ID05","age":19,"grade":"SS"}
            } 

#print(students["Collin"]) #grabs everything about collin "Collin":["ID01",30,"SSS"],
#print(students["Collin"][0]) #only grabs collins ID
#print(students["Collin"][1:]) #grabs everything about collin after ID/index 1

print(students["Alice"]["age"]) #grabs alices age
print(students["Collin"]["id"],students["Collin"]["age"])







































