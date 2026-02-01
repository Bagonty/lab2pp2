#Python Lists
mylist = ["baga" , "yarik" , "agab" ]
print(mylist)

yourlist = [1, 2, 3, 4, 5]
print(yourlist)

himlist = [True, False, True]
print(himlist)

herlist = [3.14, 2.71, 1.61]
print(herlist)

itslist = ["baga", 42, True, 3.14]
print(itslist)

#Access Items

print(mylist[0])
print(yourlist[2])
print(himlist[1])
print(herlist[2])
print(itslist[3])

#Python - Change List Items
mylist[1] = "new_name"
yourlist[3] = 10
himlist[0] = False
herlist[1] = 1.41
itslist[2] = False
print(mylist)
print(yourlist)
print(himlist)
print(herlist)
print(itslist)

#Append Items
mylist.append("last_name")
yourlist.append(99)
himlist.append(True)
herlist.append(0.577)
itslist.append("end")
print(mylist)
print(yourlist)
print(himlist)
print(herlist)
print(itslist)

#Python - Remove List Items
mylist.remove("baga")
yourlist.remove(2)
himlist.remove(False)
herlist.remove(3.14)
itslist.remove(42)
print(mylist)
print(yourlist)
print(himlist)
print(herlist)
print(itslist)

#Python - Loop Lists
for item in mylist:
    print(item)
for item in yourlist:
    print(item)
for item in himlist:
    print(item)
for item in herlist:
    print(item)
for item in itslist:
    print(item)

#Python - List Comprehension

newlist1 =[]
for x in mylist :
    if "a" in x :
        newlist1.append(x)
print(newlist1)

newlist2 = [x for x in yourlist if x > 10]
print(newlist2)

newlist3 = [x for x in himlist if x == True]
print(newlist3)

newlist4 = [x for x in herlist if x < 2.0]
print(newlist4)

newlist5 = []
for x in itslist :
    if type(x) == str :
        newlist5.append(x)
print(newlist5)

#Python - Sort Lists
mylist.sort()
yourlist.sort()
herlist.sort()
print(mylist)
print(yourlist)
print(herlist)

himlist.sort(reverse = True)
print(himlist)

mylist.sort(key = str.lower)
print(mylist)

#Python - Copy Lists

slist = mylist.copy()
print(slist)

tlist = yourlist[:]
print(tlist)

ulist = list(herlist)
print(ulist)

qlist = himlist.copy()
print(qlist)

yulist = itslist[1:4]
print(yulist)


#Join Two Lists
list1 = mylist + yourlist
print(list1)

list2 = list1 + himlist
print(list2)

list3 = list1+ herlist
print(list3)

list4 = list2 + itslist
print(list4)

list5 = mylist + itslist
print(list5)


#Python - List Methods

novilist = [ 4.6,8,3 ,5,8,7,4,3,6]
print(novilist.count(3))
novilist.reverse()
print(novilist)
novilist.insert(2, 9)
print(novilist)
novilist.pop()
print(novilist)
novilist.clear()
print(novilist)

