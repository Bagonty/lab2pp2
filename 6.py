#Python Dictionaries
thisdict = {
  "country": "Kazakhstan",
  "city": "Almaty",
  "year": 2026
}
print(thisdict)

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print(car)

phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 450000
}

print(phone)

movie = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014
}

print(movie)

#Python - Access Dictionary Items
x = thisdict["city"]
y = car.get("model")
z = phone["price"]
t = movie.get("director")
q=thisdict["year"]

#Python - Change Dictionary Items
thisdict["year"] =2025
car["year"] =2021
phone["price"] =400000
movie["year"] =2015
phone["title"]="Smartphone"
print(thisdict)
print(car)
print(phone)
print(movie)
#Python - Add Dictionary Items
thisdict["population"] = 2000000
car["color"] = "Red"
phone["storage"] = "128GB"
movie["genre"] = "Sci-Fi"
thisdict["language"]="Kazakh"
print(thisdict)
print(car)
print(phone)
print(movie)
print(thisdict)
#Python - Remove Dictionary Items
thisdict.pop("population")
car.pop("color")
phone.pop("storage")
movie.pop("genre")
thisdict.popitem()
thisdict.popitem()
print(thisdict)
print(car)
print(phone)
print(movie)
#Python - Loop Dictionaries
for key in thisdict:
    print(key)
for key in car:
    print(key)
for key in phone:
    print(key)

for key in movie:
    print(key)
for key in thisdict:
    print(thisdict[key])

for x , y in car.items():
    print(x, y)
#Python - Copy Dictionaries
mydict = thisdict.copy()
print(mydict)
yourdict = car.copy()
print(yourdict)
himdict = phone.copy()
print(himdict)
herdict = movie.copy()
print(herdict)
itsdict = dict(thisdict)
print(itsdict)
#Python - Nested Dictionaries
students = {
    "student1": {
        "name": "Arman",
        "year": 2006
    },
    "student2": {
        "name": "Aruzhan",
        "year": 2005
    },
    "student3": {
        "name": "Dias",
        "year": 2007
    }
}

cars = {
    "car1": {
        "brand": "Toyota",
        "year": 2020
    },
    "car2": {
        "brand": "BMW",
        "year": 2018
    },
    "car3": {
        "brand": "Hyundai",
        "year": 2022
    }
}

phones = {
    "phone1": {
        "model": "iPhone 14",
        "price": 600000
    },
    "phone2": {
        "model": "Samsung S23",
        "price": 450000
    },
    "phone3": {
        "model": "Xiaomi 13",
        "price": 320000
    }
}

movies = {
    "movie1": {
        "title": "Interstellar",
        "year": 2014
    },
    "movie2": {
        "title": "Inception",
        "year": 2010
    },
    "movie3": {
        "title": "Oppenheimer",
        "year": 2023
    }
}

countries = {
    "country1": {
        "name": "Kazakhstan",
        "capital": "Astana"
    },
    "country2": {
        "name": "USA",
        "capital": "Washington"
    },
    "country3": {
        "name": "Japan",
        "capital": "Tokyo"
    }
}
print(students)
print(cars)
print(phones)
print(movies)
print(countries)
#Dictionary Methods
print(thisdict.keys())
print(car.values())
print(phone.items())
print(movie.keys())
print(len(thisdict))
print(len(car))
print(type(phone))
print(type(movie))
print(type(students))
print(type(countries))
print(students.get("student2"))
print(cars.get("car3"))
print(phones.get("phone1"))
print(movies.get("movie2"))
print(countries.get("country3"))

    


