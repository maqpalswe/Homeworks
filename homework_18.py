# Paydalanıwshıdan jasın soraymız
age = int(input("Jasıńızdı kiritiń: "))

# Jasın tekseremiz
if age >= 18:
    print("Siz voyaga jetkensiz!")
else:
    print("Siz voyaga jetpegensiz!")

#2.
# Paydalanıwshıdan parol soraymız
password = input("Paroldi kiritiń: ")

# Paroldi tekseremiz
if password == "python123":
    print("Xosh kelipsiz!")
else:
    print("Parol nadurıs!")

#3.
# Өnim bahasın kiritemiz
price = int(input("Mahsulot narxini kiriting: "))

# Eger baha 500000 nan joqarı bolsa
if price > 500000:
    discount = price * 10 / 100
else:
    discount = 0

# Aqırǵı bahasın esaplaymız
final_price = price - discount

# Nátiyjeni shıǵaramız
print("Chegirma:", int(discount), "so'm")
print("Yakuniy narx:", int(final_price), "so'm")

#4.
# Aralıqtı kiritemiz
distance = int(input("Aralıqtı kiritiń: "))

# 10 km den joqarı bolsa
if distance > 10:
    price = 3000
else:
    price = 2000

# Ulıwma bahasın esaplaymız
total = distance * price

print("1 km bahası:", price, "swm.")
print("Ulıwma bahası:", total, "sum.")


#5.
# Buyırtpa bahasın kiritemiz
price = int(input("Buyırtpa bahası: "))

# Jetkiziw bahasın tekseremiz
if price > 100000:
    print("Jetkiziw biypul!")
    total = price
else:
    delivery = 15000
    total = price + delivery
    print("Jetkerip beriw:", delivery, "sum.")

print("Jámi tólem:", total, "sum.")


#6.
# Ball kiritemiz
ball = int(input("Ballıńızdı kiritiń: "))

# Ballǵa qarap bahalaymız
if ball >= 90:
    print("Sizdiń bahańız: A'lo")
elif ball >= 75:
    print("Sizdiń bahańız: Jaǵsı")
elif ball >= 60:
    print("Sizdiń bahańız: Qanaatlandırarlı")
else:
    print("Sizdiń bahańız: Qanaatlandırarsız")

#7.
# Transport atları hám narxları
transports = ["Avtobus", "Metro", "Taksi", "Velosiped"]
prices = [2000, 1700, 15000, 1000]

# Transportlardı ekranga shıǵaramız
print("===== TRANSPORT TAŃLAW =====")

for i in range(4):
    print(i + 1, transports[i])

# Paydalanıwshıdan transport soraymız
choice = int(input("Transporttı tańlań: "))

# Tańlanǵan transporttı shıǵaramız
if choice >= 1 and choice <= 4:
    print("Siz", transports[choice - 1], "transportın tańladıńız.")
    print("Narxı:", prices[choice - 1], "so'm")

#8.
# Miyweler dizimi
fruits = ["alma", "banan", "uzum", "anor", "shaftoli"]

# Miyweniń atın soraymız
name = input("Meva atın kiritiń: ")

# Dizimde bar yamasa joqlıǵın tekseremiz
if name in fruits:
    print(name, "ro'yxatta mavjud!")
else:
    print(name, "ro'yxatta joq!")

#9.
# Oqıwshılar dizimi
students = ["Ali", "Vali", "Sardor", "Malika", "Madina"]

# Oqıwshı atın soraymız
name = input("Ism kiritiń: ")

# Oqıwshını tekseremiz
if name in students:
    print("O'quvchi ro'yxatta mavjud!")
    print("Birinshi hárpi:", name[0])
else:
    print("O'quvchi ro'yxatta joq!")

#10.
# Sanlar dizimi
numbers = [12, 5, 8, 17, 20, 3, 10, 7]

# Hárbir sandı tekseremiz
for i in numbers:
    if i % 2 == 0:
        print(i, "- Jup san")
    else:
        print(i, "- Taq san")

#11.
# Sanlar dizimi
numbers = [2, 5, 8, 11, 14, 17]

# Hárbir elementti tekseremiz
for i in range(len(numbers)):
    if numbers[i] < 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

# Ózgergen dizimdi shıǵaramız
print(numbers)

#12.

# Tawarlardıń atları hám bahaları
products = ["Go'sht", "Non", "Sut", "Tuxum", "Guruch"]
prices = [90000, 4000, 12000, 1800, 15000]

# Tawarlardı ekranga shıǵaramız
print("Mahsulotlar:")

for i in range(len(products)):
    print(i + 1, products[i], "-", prices[i], "so'm")

# Qaysı tawar kerek ekenin soraymız
choice = int(input("Qaysı mahsulot kerek? "))

# Tawar sanın soraymız
count = int(input("Qansha kerek? "))

# Ulıwma summanı esaplaymız
total = prices[choice - 1] * count

print("Mahsulot:", products[choice - 1])
print("Soni:", count)
print("Ulıwma summa:", total, "so'm")


#13.
# Tawarlar hám bahaları
products = ["Non", "Sut", "Go'sht", "Olma", "Banan"]
prices = [4000, 12000, 90000, 8000, 15000]

# Tawar atın soraymız
name = input("Qanday mahsulot almoqchisiz? ")

# Tawardı izleyimiz
for i in range(len(products)):
    if products[i] == name:
        count = int(input(name + " qancha kerak? "))

        # Ulıwma bahasın esaplaymız
        total = prices[i] * count

        print("Ulıwma summa:", total, "so'm")
        break
else:
    print("Bunday tovar jo'q!")


#14.
# Oqıwshılardıń bahaları
grades = [
    [5, 4, 3],
    [4, 5, 5],
    [3, 2, 4]
]

# Barlıq bahalardı kórsetemiz
for row in grades:
    for grade in row:
        print(grade)

# 5 bahalardı 4 ke ózgertemiz
for i in range(len(grades)):
    for j in range(len(grades[i])):
        if grades[i][j] == 5:
            grades[i][j] = 4

# 2 bahalardı 3 ke ózgertemiz
for i in range(len(grades)):
    for j in range(len(grades[i])):
        if grades[i][j] == 2:
            grades[i][j] = 3

# Ózgergen dizimdi shıǵaramız
print(grades)

#15.
# Tawarlar, bahaları hám sanları
products = [
    ["Non", 4000, 10],
    ["Sut", 12000, 5],
    ["Go'sht", 90000, 2],
    ["Olma", 8000, 0]
]

# Hárbir tawardı tekseremiz
for i in range(len(products)):
    name = products[i][0]
    count = products[i][2]

    print(i + 1, name, "Sani:", count)

    # Tawar sanın tekseremiz
    if count >= 5:
        print("Status: Jetkilikli")
    else:
        print("Status: Az qalǵan")
