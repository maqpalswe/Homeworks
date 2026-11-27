
      # HOMEWORK 

#1.
# 5 miywe atınan ibarat list jaratamız
fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape']

# Listti ekranǵa shıǵaramız
print(fruits)

#2.
# 5 sannan ibarat list
numbers = [10, 20, 30, 40, 50]

# Birinshi element
print(numbers[0])

# Aqırǵı element
print(numbers[-1])

# Úshinshi element
print(numbers[2])

#3.
# Rengler dizimin jaratamız
colors = ['red', 'green', 'blue', 'yellow']

# Green ornına black jazamız
colors[1] = 'black'

# Yellow ornına white jazamız
colors[3] = 'white'

# Jańa listti shıǵaramız
print(colors)

#4.
# Oqıwshılar atları jazılǵan list
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# len() járdeminde elementler sanın tabamız
print(len(students))

#5.
# Sanlardan ibarat list
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# 2-indexten 5-indexke shekem elementlerdi alamız
print(numbers[2:5])

#6.
# Háriplerden ibarat list
letters = ['a', 'b', 'c', 'd', 'e', 'f']

# [::-1] listti keri tártipte shıǵaradı
print(letters[::-1])

#7.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[::2])

#8.
# Oqıwshılar haqqında maǵlıwmat
students = [
    ['Ali', 90, 'English'],
    ['Vali', 85, 'Math'],
    ['Hasan', 95, 'Python']
]

# Birinshi oqıwshınıń maǵlıwmatların alamız
print(students[0][0])  # Atı
print(students[0][1])  # Bahası
print(students[0][2])  # Pán

#9.
# Oqıwshılar hám olardıń bahaları
students = [
    ['Ali', 90],
    ['Vali', 85],
    ['Hasan', 95]
]

# Aliniń bahasın 90 nan 100 ge ózgertemiz
students[0][1] = 100

# Jańa listti shıǵaramız
print(students)

#10.
# Programmalaw tilleri dizimi
programming = [
    ['HTML', 'CSS'],
    ['Python', 'JavaScript'],
    ['Java', 'C++']
]

# Python elementin shıǵaramız
print(programming[1][0])

# JavaScript elementin shıǵaramız
print(programming[1][1])

#11.
# Sanlardan ibarat list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1-indexten baslap hár úshinshi elementti alamız
print(numbers[1::3])


#12.
# Berilgen sanlar dizimi
numbers = [12, 7, 8, 15, 20, 33, 44, 51, 60]

# Tek jup sanlardı alamız
print(numbers[::2])

#13.
# Berilgen sanlar dizimi
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]

# Qaytalanǵan elementlerdi alıp taslaymız
print(numbers[0:3] + numbers[4::2])

#14.
# Berilgen sanlar dizimi
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Birinshi listti alamız
list1 = numbers[0:3]

# Ekinshi listti alamız
list2 = numbers[4:7]

# Eki listti ekranǵa shıǵaramız
print("1-list:", list1)
print("2-list:", list2)

#15.
# Berilgen sanlar dizimi
numbers = [10, 20, 30, 40, 50]

# 20 sanın waqıtsha saqlaymız
temp = numbers[1]

# 40 sanın 20 ornına qoyamız
numbers[1] = numbers[3]

# 20 sanın 40 ornına qoyamız
numbers[3] = temp

# Jańa listti shıǵaramız
print(numbers)

#16.
# Studentler atları dizimi
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# Ali atın waqıtsha saqlaymız
temp = students[0]

# Olim atın birinshi orınǵa qoyamız
students[0] = students[4]

# Ali atın aqırǵı orınǵa qoyamız
students[4] = temp

# Jańa dizimdi shıǵaramız
print(students)

#17.
# Studentler hám olardıń balları
students = [
    ['Ali', 85],
    ['Vali', 90],
    ['Hasan', 75],
    ['Husan', 95]
]

# Ali haqqındaǵı maǵlıwmattı saqlaymız
temp = students[0]

# Hasan haqqındaǵı maǵlıwmattı Ali ornına qoyamız
students[0] = students[2]

# Ali haqqındaǵı maǵlıwmattı Hasan ornına qoyamız
students[2] = temp

# Jańa dizimdi shıǵaramız
print(students)

#18 
# Miyweler dizimin jaratamız
fruits = ['Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']

# Miyweler dizimin ekranǵa shıǵaramız
print("Miyweler:")

# Miywelerdi nomerleri menen shıǵaramız
print("1.", fruits[0])
print("2.", fruits[1])
print("3.", fruits[2])
print("4.", fruits[3])
print("5.", fruits[4])

# Paydalanıwshıdan miywe tańlawın soraymız
choice = int(input("Qaysı miyweni tańlaysız? "))

# Tańlanǵan miyweni shıǵaramız
print("Siz", fruits[choice - 1], "miywesin tańladıńız!")

#19.
# Miyweler dizimi
fruits = ['apple', 'banana', 'orange']

# Listtiń aqırına mango qosamız
fruits.append('mango')

# 2-indekske strawberry jaylastıramız
fruits.insert(2, 'strawberry')

# Jańa listti shıǵaramız
print(fruits)

#20.
# Miyweler dizimi
fruits = ['apple', 'banana', 'apple', 'orange', 'apple', 'kiwi']

# Apple sanın esaplaymız
print("Apple sani:", fruits.count('apple'))

#21.
# Mashinalar dizimi
cars = ['BMW', 'Mercedes', 'Audi', 'Tesla']

# BMW elementin óshiremiz
cars.remove('BMW')

# Qalǵan listti shıǵaramız
print(cars)


#22.
# Sanlar dizimi
numbers = [10, 20, 30, 40, 50]

# Aqırǵı elementti óshiremiz
deleted = numbers.pop()

# Óshirilgen elementti shıǵaramız
print("Óshirilgen element:", deleted)

# Qalǵan listti shıǵaramız
print("Qalǵan list:", numbers)

#23.
# Programmalaw tilleri dizimi
languages = ['Java', 'C++', 'Python', 'JavaScript', 'PHP']

# Python elementiniń indeksin tabamız
print("Python indeksi:", languages.index('Python'))

#24
# Sanlar dizimi
numbers = [45, 12, 89, 3, 21, 67, 10]

# Sanlardı ósiw tártibinde tártiplestiremiz
numbers.sort()

# Nátiyjeni shıǵaramız
print(numbers)
