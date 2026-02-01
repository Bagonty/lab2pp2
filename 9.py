#Python For Loops
fruits = ["apple", "pear", "cherry"]

for x in fruits:
    print(x)

for i in range(5):
    print(i)

word = "Python"

for letter in word:
    print(letter)

car = {
    "brand": "Toyota",
    "year": 2020
}

for key in car:
    print(key, car[key])

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n > 3:
        print(n)

#while Loops

i = 0

while i < 5:
    print(i)
    i += 1

x = 1

while x <= 5:
    print(x)
    x += 1

num = 10

while num > 0:
    print(num)
    num -= 2

password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted")

i = 0

while True:
    print(i)    
    if i == 3:
        break
    i += 1

# with break and continue 

for i in range(10):
    if i == 5:
        break
    print(i)

x = 0

while True:
    print(x)
    if x == 3:
        break
    x += 1

for i in range(6):
    if i == 3:
        continue
    print(i)

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        continue
    print(n)

for i in range(10):
    if i == 2:
        continue
    if i == 6:
        break
    print(i)
