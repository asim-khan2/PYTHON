dic = {"Name" : "Asim", "Age" : 22, "Add." : "Dhanaura urf murad nagar"}
print(dic)
print(dic["Name"])

dic1 = {
    342 : "Asim",
    344 : "Danish",
    341 : "Najim"
}

print(dic1[341])

#get method return none
print(dic1.get(344))

# 354 not present in the dictionary this give error to us 
#print(dic1[354])

#354 not peresent in the dictionary get fun. return none
print(dic1.get(354))

# key method to give all key peresent in the dictionary
print(dic1.keys())

for key in dic1: # for loop print key value
    print(dic1[key])

# item method give key value pairs
print(dic1.items())

for key, value in dic1.items(): # this for loop print key and value 
    print(key , value)