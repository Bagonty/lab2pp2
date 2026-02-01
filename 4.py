#Python Tuples
mytuple = ("a","b","c","d","e")
print(mytuple)
print(type(mytuple))
yourtuple = (10,20,30,40,50)
print(yourtuple)
himtuple = (True, False, True, False)
print(himtuple)
hertuple = (3.14, 2.71, 1.61)
print(hertuple)
itstuple = ("baga", 42, True, 3.14)
print(itstuple)
#Access Tuples
print(mytuple[0])
print(yourtuple[2:3])
print(himtuple[:3])
print(hertuple[:1])
print(itstuple[-2:])
#Python - Update Tuples
mylist = list(mytuple)
mylist[1] = "z"
mytuple = tuple(mylist)
print(mytuple)
yourlist = list(yourtuple)
yourlist[3] = 99
yourtuple = tuple(yourlist)
print(yourtuple)
himlist = list(himtuple)
himlist[0] = False
himtuple = tuple(himlist)
print(himtuple)
herlist = list(hertuple)
herlist[2] = 1.41
hertuple = tuple(herlist)
print(hertuple)
itslist = list(itstuple)
itslist[2] = False
itstuple = tuple(itslist)
print(itstuple)
#Python - Unpack Tuples
(a, b, c, d, e) = mytuple
print(a)

fruits = ("apple", "banana", "cherry")
(x, y, z) = fruits
print(y)

colors = ("red", "green", "blue", "yellow")
(r, g, b, y) = colors
print(b)

numbers = (1, 2, 3, 4, 5)
(n1, n2, n3, n4, n5) = numbers
print(n4)

points = (10, 20, 30)
(p1, p2, p3) = points
print(p1)

#Python - Loop Tuples
for item in mytuple:
    print(item)
for item in yourtuple:
    print(item)
for item in himtuple:
    print(item)
for item in hertuple:
    print(item)
for item in itstuple:
    print(item)

#Python - Join Tuples
tuple1 = mytuple + yourtuple
print(tuple1)
tuple2 = himtuple + hertuple
print(tuple2)
tuple3 = itstuple + fruits
print(tuple3)
tuple4 = colors + numbers
print(tuple4)
tuple5 = yourtuple + itstuple
print(tuple5)
#Tuple Methods
print(mytuple.count("a"))
print(yourtuple.count(20))
print(himtuple.count(True))
print(hertuple.index(3.14))
print(itstuple.index(42))