#Python Match Case Statement
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")

choice = 2

match choice:
    case 1:
        print("Start game")
    case 2:
        print("Settings")
    case 3:
        print("Exit")

grade = "B"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Unknown grade")

operation = "+"

match operation:
    case "+":
        print(10 + 5)
    case "-":
        print(10 - 5)
    case "*":
        print(10 * 5)
    case "/":
        print(10 / 5)

role = "admin"

match role:
    case "admin":
        print("Full access")
    case "user":
        print("Limited access")
    case "guest":
        print("Read only")
    case _:
        print("Unknown role")
