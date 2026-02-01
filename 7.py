#Python If Statement
a = 10
b = 20
if b > a:
    print("b is greater than a")

temperature = 30

if temperature > 25:
    print("It is hot outside")
    print("Drink more water")
    print("Stay in the shade")

password = "python123"

if len(password) >= 8:
    print("Password length is OK")
    print("Password accepted")
    print("You can log in")

score = 85

if score >= 70:
    print("You passed the exam")
    print("Good job")
    print("Keep studying")

balance = 5000

if balance >= 3000:
    print("You have enough money")
    print("Purchase approved")
    print("Thank you for shopping")#
#Multiple Elif Statements
age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


temperature = 5

if temperature >= 30:
    print("Very hot")
elif temperature >= 20:
    print("Warm")
elif temperature >= 10:
    print("Cool")
else:
    print("Cold")

level = 2

if level == 3:
    print("Admin access")
elif level == 2:
    print("User access")
elif level == 1:
    print("Guest access")
else:
    print("No access")
score = 88

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

balance = 1200

if balance >= 5000:
    print("Gold client")
elif balance >= 2000:
    print("Silver client")
elif balance >= 500:
    print("Bronze client")
else:
    print("Insufficient funds")

#Else Without Elif
a = 50
b = 100

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

name1 = "Alex"
name2 = "Bob"

if name1 == name2:
    print("Names are the same")
else:
    print("Names are different")

is_raining = True

if is_raining:
    print("Take an umbrella")
else:
    print("Weather is good")

numbers = [1, 2, 3]
numbers2 = [1, 2, 3, 4]

if len(numbers) > len(numbers2):
    print("First list is longer")
else:
    print("Second list is longer")

car = {
    "brand": "Toyota",
    "year": 2020
}

if "brand" in car:
    print("Brand exists")
else:
    print("Brand not found")
#Python Shorthand If
a = 10
b = 5
if a > b: print("a is greater than b")
name = "Alex"
if name == "Alex": print("Hello Alex")
is_admin = True
if is_admin: print("Access granted")
numbers = [1, 2, 3]
if 2 in numbers: print("2 is in the list")
car = {"brand": "Toyota", "year": 2020}
if "brand" in car: print("Brand key exists")
#Python Logical Operators
a = 50
b = 20
c = 100

if a > b and c > a:
    print("Both conditions are True")

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

x = 5

if x < 0 or x > 10:
    print("Number is out of range")

is_logged_in = False

if not is_logged_in:
    print("Please log in")
#Nested If Statements
x = 30

if x > 10:
    print("Above 10")

    if x > 20:
        print("Above 20")
age = 19

if age >= 18:
    print("Adult")

    if age >= 21:
        print("Can buy alcohol")
    else:
        print("Too young for alcohol")
is_logged_in = True
is_admin = False

if is_logged_in:
    print("User logged in")

    if is_admin:
        print("Admin panel")
    else:
        print("User panel")
score = 85

if score >= 60:
    print("Exam passed")

    if score >= 90:
        print("Excellent")
    else:
        print("Good result")
balance = 3000

if balance > 0:
    print("Account active")

    if balance >= 5000:
        print("Premium account")
    else:
        print("Standard account")
#Python Pass Statement
a = 10
b = 20

if b > a:
    pass
age = 17

if age >= 18:
    pass
else:
    print("Access denied")
x = 5

if x > 0:
    pass
print("Program continues")
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
def my_function():
    pass
my_function()

