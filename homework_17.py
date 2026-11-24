#1.
# Miyweler dizimi
fruits = ['apple', 'banana', 'orange', 'kiwi']

# Hárbir miyweni ekranǵa shıǵaramız
for fruit in fruits:
    print(fruit)
  
#2.
# Atlar dizimi
names = ['ali', 'vali', 'hasan', 'husan']

# Atlardı úlken háriplerge ózgertemiz
for name in names:
  print(name.upper())

#3.
# Mashinalar dizimi
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']

# Hárbir mashina atınıń birinshi háribin shıǵaramız
for car in cars:
    print(car[0])

#4.
# Mámleketler dizimi
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']

# Mámleket atların kishi háriplerge ózgertemiz
for country in countries:
    print(country.lower())


#5.
# Atlar dizimi
names = ['ali', 'sardor', 'abdulloh', 'aziz']

# Hárbir attıń hárip sanın tabamız
for name in names:
    print(name, "-", len(name), "ta hárip")

#6.
# Haywanlar dizimi
animals = ['cat', 'dog', 'lion', 'tiger']

# range() járdeminde indekslerdi alamız
for i in range(4):
    animals[i] = animals[i].upper()

# Jańa dizimdi shıǵaramız
print(animals)

#7.
# Atlar dizimi
names = ['ali', 'vali', 'sardor', 'aziz']

# Atlardı úlken háriplerge ózgertemiz
for i in range(len(names)):
    names[i] = names[i].upper()

# Nátiyjeni shıǵaramız
print(names)

#8.
# Atlar dizimi
names = ['ali', 'hasan', 'husan', 'sardor']

# Atlardıń birinshi háribin úlkeytemiz
for i in range(len(names)):
    names[i] = names[i].capitalize()

# Nátiyjeni shıǵaramız
print(names)

#9.
# Atlar dizimi
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']

# Jup indekslerdegi atlardı shıǵaramız
for i in range(0, len(names), 2):
    print(names[i])

#9.
# Atlar dizimi
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']

# Jup indekslerdegi atlardı shıǵaramız
for i in range(0, len(names), 2):
    print(names[i])

#10.
# Haywanlar dizimi
animals = ['tiger', 'lion', 'elephant', 'rabbit']

# Birinshi hám aqırǵı háriplerin shıǵaramız
for animal in animals:
    print(animal[0], "-", animal[-1])

#11.
# Sózler dizimi
words = ['python', 'programming', 'computer', 'developer']

# Birinshi hám aqırǵı háriplerin úlkeytemiz
for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:-1] + words[i][-1].upper()

# Nátiyjeni shıǵaramız
print(words)

#12.
# Mashinalar dizimi
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']

# Mashina atların úlken háriplerge ózgertemiz
for i in range(len(cars)):
    cars[i] = cars[i].upper()

# Nátiyjeni shıǵaramız
print(cars)


#13.
# Paydalanıwshıdan atın soraymız
name = input("Atıńızdı kiritiń: ")

# Neshe márte shıǵarıw kerek ekenin soraymız
n = int(input("Neshe márte shıǵarılsın: "))

# Attı kórsetilgen márte shıǵaramız
for i in range(n):
    print(name)


#14.
# Bos miyweler dizimin jaratamız
fruits = []

# Paydalanıwshıdan miyweler sanın soraymız
n = int(input("Neshe miywe kirgizbekshisiz: "))

# Miywelerdi birme-bir kirgizemiz
for i in range(n):
    fruit = input(str(i + 1) + "-miyweni kiritiń: ")

    # Miyweni dizimge qosamız
    fruits.append(fruit)

# Barlıq miywelerdi shıǵaramız
print("Miyweler:", fruits)

#15.
# Bos reńler dizimin jaratamız
colors = []

# 5 reń kirgiziwdi soraymız
for i in range(5):
    color = input(str(i + 1) + "-reńdi kiritiń: ")

    # Reńlerdi dizimge qosamız
    colors.append(color)

# Jaǵımlı kóretuǵın reńlerdi shıǵaramız
print("Siz jaqsı kóretuǵın reńler:")

for color in colors:
    print(color)







