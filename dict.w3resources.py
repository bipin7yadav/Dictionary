# 2. Write a Python script to add a key to a dictionary.
# a={0:10,1:20}
# a[2]=30
# print(a)

# a.update({3:40})
# print(a)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# # dic1.update(dic2)
# # dic1.update(dic3)
# # print(dic1)
# dic4={}
# for d in (dic1,dic2,dic3) :
# 	dic4.update(d)
# print(dic4)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
# a={1:10,2:20,3:30,4:40}
# if 3 in a:
# 	print("It is present")
# else:
# 	print("It is absent")


# 5. Write a Python program to iterate over dictionaries using for loops.
# a={1:10,2:20,3:30,4:40,5:50}
# for k,y in a.items():
# 	print(k,"=",y)


# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# a={}
# for i in range(1,16):
# 	a.update({i:i*i})
# print(a)

# 8. Write a Python script to merge two Python dictionaries.
# a={1:10,2:20,3:30,4:40,5:50,6:60}
# b={7:70,8:80,9:90,10:100}
# a.update(b)
# print(a)



# 10. Write a Python program to sum all the items in a dictionary.
# a={1:10,2:20,3:30,4:40,5:50}
# sum1=0
# for i in a.values():
# 	sum1+=i
# print(sum1)


# 11. Write a Python program to multiply all the items in a dictionary.
# a={1:2,2:5,3:7,4:1}
# v=1
# for i in a.values():
# 	v*=i
# print(v)

# 12. Write a Python program to remove a key from a dictionary.
# a={"v":6,"K":8,"y":9}
# # if "v" in a:
# 	del a["v"]
# a.pop("v")
# print(a)

# 13. Write a Python program to map two lists into a dictionary.
# names=["Nikhil","Manoj","Bipin","Suryasen"]
# marks=[89,76,96,84]
# dictionary=dict(zip(names,marks))
# print(dictionary)


# 14. Write a Python program to sort a given dictionary by key.

# a={"manoj":10,"nikhil":9,"bipin":8,"suryasen":7}
# for i in sorted(a.items()):
# 	print(i)
# print(sorted(a))

# 15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor
# a={"a":2,"b":8,"c":98,"d":48}
# for i in sorted(a.values()):
# 	print(i)

# 17. Write a Python program to remove duplicates from Dictionary.#Doubt

# 18. Write a Python program to check a dictionary is empty or not.
# a={}
# if len(a)==0 :
# 	print("It is an empty Dictionary")
# else:
# 	print("It is not an Empty dict")
# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1={"a":100,"b":200,"c":300}
# d2={"a":400,"b":500,"c":600}
# for i in d1.values():
# 	print(i)
# 	for j in (d2.values()[i]):
		# print(j)##Doubt

# 20. Write a Python program to print all unique values in a dictionary.
# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print(set(i for dic in a for i in dic.values()))###DOUBT
# v=[]
# for i in a:
# 	for j in i.values():
# 		v.append(j)
# print(set(v))


# 28. Write a Python program to sort a list alphabetically in a dictionary. Go to the editor
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# k={}
# for i,j in num.items():
# 	k[i]=sorted(j)
# print(k)


# 29. Write a Python program to remove spaces from dictionary keys. Go to the editor
# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# a={}
# for i,j in student_list.items():
# 	# a[i.translate({32:None})]=j
# 	a[''.join(i.split())]=j
# print(a)


# 30. Write a Python program to get the top three items in a shop. Go to the editor
# Sample={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# a={}
# b=dict(sorted((x,y) for (y,x) in Sample.items()))
# print(dict(b))
# c=([(x,y) for (y,x) in b.items()])
# d=(dict(list(c)[-3:]))
# print(d)
# for i in d.items():
# 	print(i)


# 31. Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# print('key','value','count')
# for i,j in dict_num.items():
# 	count +=1
# 	print(i,"  " ,j,"  " ,count)

# 32. Write a Python program to print a dictionary line by line.
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for i in students:
# 	print(i)
# 	for j in students[i]:
# 		print(j,':',students[i][j])

# 34. Write a Python program to count number of items in a dictionary value that is a list.
# dict1={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=0
# for i in dict1.values():
# 	for j in i :
# 		count +=1
# print(count)

# 35. Write a Python program to sort Counter by value. Go to the editor
# Sample_data={'Math':81, 'Physics':83, 'Chemistry':87}
# v=(sorted([(key,value) for (key,value) in Sample_data.items()]))
# print(v)
# # n=(sorted([(v, k) for k, v in Sample_data.items()], reverse=True))
# # print(n)

# 36. Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
# Sample_lists=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# count=0
# a={}
# for i in Sample_lists[0]:
# 	count+=1
# 	if count==2:
# 		break
# 	# print(i)
# 	for j in Sample_lists[1]:
# 		a[i]={j}
# 		print(a)


# print(chr(8560))
# a={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
# inp=int(input("ENTER NUMBER:"))
# print(inp)
# v=len(str(inp))
# print(v)
# for i in a.items():
# 	print(i)

# roman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
#               50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
# int= int(input("Enter a number: "))
# print_order= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

# for x in print_order:
#     if int != 0:
#         quotient= int//x
#         if quotient != 0:
#             for y in range(quotient):
#                 print(roman[x], end="")
#         int = int%x




# employee=['emp1','emp2','emp3']
# keys=["name","age","work"]
# values=[
#         ['manoj','22','Stu_M',],
#         ['Bipin','19','Stu_B'], 
#         ['Nikhil','20','Stu_N'],
#         #["Apan",'17','Stu_A']
#        ]
# dict2={}
# for i in range(len(employee)):
#     dict1={}
#     for j in range(len(employee)):
#         dict1[keys[j]]=values[i][j]
#     dict2[employee[i]]=dict1
# print(dict2)

# a=[["suraj","HR",21,22000],["Pawan","manager",22,20000],["ashok","fm",19,10000]]
# b=["NAME","DESIG","AGE","SALARY"]
# c=["emp1","emp2","emp3"]   
# d={}
# d1={}
# for i in range(len(c)):
#     for j in range(len(c)):
#         d[b[j]]=a[i][j]
#         d1[c[i]]=d
# print(d1)






##############################CODES DOPE##############################
#1. and 2. Ask user to give name and marks of 10 different students. Store them in dictionary.
# a={}
# for i in range(5):
# 	n=input("Enter Name: ")
# 	m=int(input("Enter Marks: "))
# 	a[n]=m
# print(a)
# a={'ram':79,'key':65,'jay':45}
# v=dict(sorted((key,value) for (value,key) in a.items()))
# print((v))
# k=dict((key,value) for (value,key) in v.items())
# print(k)


# 3.Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
# dictionary={}
# for i in range(4):
# 	n=input("Emter word:")
# 	op=input("Enter opp word")
# 	dictionary[n]=op
# print(dictionary)


##4. & 5.Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
# dic="MISSISSIPPI"
# v=set(dic)
# j={}
# for i in v:
#     k=dic.count(i) 
#     j[i]=k
# print(j)
# d_sorted = sorted(zip(j.values(), j.keys()))
# print(d_sorted)
# a={}
# for i in d_sorted:
# 	a[i[1]]=i[0]
# print(a)

# 6.Take a list containg only strings. Now, take a string input from user and rearrange the elements of the list according to the number of occurence of the string taken from user in the elements of the list.
# a=["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# b="bug"
# c={}
# for i in a:
# 	count=0
# 	for j in i.split():
# 		if j==b:
# 			count +=1
# 	c[i]=count
# print(c)
# # print(count)
# # n=dict(sorted([(v, k) for k, v in c.items()], reverse=True))
# # print(dict(n))
# # l=dict((k,v) for(v,k) in n.items())
# # print(list(l.keys()))


# #also

# k=[]
# for j in sorted(c):
# 	k.append(j)
# # k.reverse()
# print(k)


######################### pynative ##########################

# s = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(s["class"]["student"]["marks"]["history"])
# a=[]
# for i in (s["class"]["student"]["marks"]).values() :
#     a.append(i)
# print(a[1],"history")


# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

# resDict = dict.fromkeys(employees, defaults)
# print(resDict)

# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }
# m={}

# keys = ["name", "salary"]
# for i in keys:
#     m[i]=sampleDict[i]
# print(m)
# n={}
# key=["city","age"]
# for i in key:
#     n[i]=sampleDict[i]
# print(n)



#Exercise 7: Check if a value 200 exists in a dictionary
# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sampleDict.values():
#     print("True")

# Exercise 8: Rename key city to location in the following dictionary

# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sampleDict["location"]=sampleDict["city"]
# sampleDict.pop("city")




# # or
# # sampleDict["location"]= sampleDict.pop("city")
# print(sampleDict)


# Exercise 9: Get the key of a minimum value from the following dictionary
# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# b=(min((x,y) for (x,y) in sampleDict.items()))
# print(b[0])

# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# minV = min(sampleDict.values())
# for v,k in sampleDict.items():
#   if  minV== k:
#     print(v)



# a=["a","b","c","d","e"]
# b=[1,2,3,4,5]
# print(dict(zip(a,b)))

# from heapq import nlargest
# FruitDict = {'Apple': 600, 'Banana': 515,'Orange':214,'Guava':1116}  
# two_highest_values = nlargest(3, FruitDict, key=FruitDict.get)
# print(two_highest_values) 

# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sampleDict["emp3"]["salary"]=8500
# print(sampleDict)


# a=[{"start":"2018-9-1","end":"2017-01-2"},{"start":"2019-9-1","end":"2018-01-1"}]
# b=[]
# for i in a:
#     for j in i.values():
#         b.append(j.split("-"))
# print(b)
# # c=int(b[0][0])-int(b[1][0]),int(b[0][1])-int(b[1][1]),int(b[0][2])-int(b[1][2])
# # print(c)
# # d=int(b[2][0])-int(b[3][0]),int(b[2][1])-int(b[3][1]),int(b[2][2])-int(b[3][2])
# # print(d)
# # e=c[1]+c[0]*12
# # print(e,"-months")
# # f=d[1]+d[0]*12
# # print(f,"-months")
# print(len(b))
# start=[]
# end=[]
# result=[]
# for i in range(0,len(b),2):
#     start.append(b[i])
# print(start)
# for j in range(1,len(b),2):
#     end.append(b[j])
# print(end)
# for i in range(len(start)):
#     for j,k in zip(start[i],end[i]):
#         result.append(int(j)-int(k))
# print(result)


# a=[["suraj","HR",21,22000],["Pawan","manager",22,20000],["ashok","fm",19,10000]]
# b=["NAME","DESIG","AGE","SALARY"]
# c=["emp1","emp2","emp3"]   
# d={}
# d1={}
# for i in range(len(c)):
#     for j in range(len(c)):
#         d[b[j]]=a[i][j]
#         d1[c[i]]=d
# print(d1)










info=['name','salery','destination']
nam=['manoj','bipin','nikhil']
sal=[35000,36000,37000]
dest=['Delhi','Mumbai','Indore']
d=[]
d.append(nam)
d.append(sal)
d.append(dest)
print(d)
a={}
m={}
for i in range(len(sal)):
    b={}
    for j in range(len(sal)):
        b[info[j]]= d[j][i]
        a[i]=b
    
    print(b)



# for i in b[0]:
#     for j in b[1]:
#         if i>b:
#             print(int(i)-int(j))


# a=["name","age","salary","designation"]
# b=[["bipin","manoj","nikhil","vijay"],
# [10,23,29,34],
# [1000,22000,7000,5000],
# ["hr","servant","engineer","telecaller"]]
# c=["empl1","empl2","empl3","empl4"]
# d={}
# for i in range(len(c)):
#     e={}
#     for j in range(len(c)):
#         e[a[j]]=b[j][i]
#         d[c[i]]=e
# print(d)
