#Python Operators
#1
sum1 = 15 + 30
sum2 = 50 + sum1
sum3 = sum2 + 2
sum4 = sum3 +22
sum5 = sum4 + 100
print(sum1 , end=",")
print(sum2 , end=",")
print(sum3 , end=",")
print(sum4 , end=",")
print(sum5)

#Python Arithmetic Operators

x = 33
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Python Comparison Operators
x = 99
y = 2.5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Python Logical Operators

s = 5
print(s > 0 and s < 10)

k = 7

print(k < 5 or k > 10)

d = 23

print(not(d > 3 and d < 10))

rd = 23
print(not(rd < 20 or rd > 30))

qa = 56
print(qa > 50 and qa < 60)


#Python Identity Operators

x = ["baga", "agab"]
y = ["baga", "agab"]
z = x

print(x is z)
print(x is y)
print(x == y)


oo = ["wuw", "ahaha"]
uu = ["wuw", "ahaha"]

print(oo is not uu)


xxs = ["bird", "wolk"]
wds = ["bir", "banana"]

print(xxs is not wds)

qq = ["cat","not cat"]
ddd = qq
print(qq is ddd)

tat = ["sun", "moon"]
mat = ["sun", "moon"]
print(tat is not mat)


#Python Membership Operators

animals = ["tiger", "lion", "dodo", "elephant", "giraffe"]

print("tiger" in animals)


subjects = [ "Mathematics", "Science", "English", "History", "Geography"]
print("Art" not in subjects)


text = "salam baga"

print("a" in text)
print("sa" in text)
print("salam" not in text)

quantity = [10, 20, 30, 40, 50]
print(25 in quantity)
print(40 not in quantity)

insects = ["ant", "bee", "butterfly", "mosquito"]
print("bee" in insects)

#Python Bitwise Operators

x = 5
y = 3
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(x >> 1)


#Python Operator Precedence

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
result3 = 20 / 4 + 2
result4 = 20 / (4 + 2)
result5 = 3**4/4-2
print(result1, end=", ")
print(result2, end=", ")
print(result3, end=", ")
print(result4, end=", ")
print(result5)