


#Homework
#1-tapsirms
# 5 miyweden ibarat list jaratiw
miyweler = ['Olma', 'Banan', 'Uzum', 'Anor', 'Nok']

# Barliq miywelerdi ekranga shigariw
print(miyweler)

#2-tapsirma
# 5 qala atinan list jaratiw
qalalar = ['Toshkent', 'Nukus', 'Xiva', 'Buxoro', 'Samarqand']

# Birinshi hám aqirgi qalani shigariw
print("Birinshi shahar:", qalalar[0])
print("Oxirgi shahar:", qalalar[-1])

#3-tapsirma
# 4 rennen ibarat list jaratiw
renler = ['Qizil', 'Yashil', "Ko'k", 'Sariq']

# Renlerdi shigariw
print("Ranglar:", renler)

# Paydalaniwshidan index soraw
index = int(input("Index kiriting: "))

# Tanlangan rendi shigariw
print("Tanlangan rang:", renler[index])

#4-tapsirma
# 5 attan ibarat list jaratiw
names = ['Anvar', 'Jasur', 'Madina', 'Sardor', 'Bekzod']

# 2-indekstegi atti Ali ge ozgertiw
names[2] = 'Ali'

# Natijeni shigariw
print(names)

#5-tapsirma
# 5 sannan ibarat list jaratiw
sanlar = [10, 20, 30, 40, 50]

# 0, 2 ham 4-indekstegi sanlardi shigariw
print("Birinshi son:", sanlar[0])
print("Ushinshi son:", sanlar[2])
print("Beshinshi son:", sanlar[4])

#6-tapsirma
# Kafe menusin jaratiw
awqatlar = ['Sorpa', 'Palaw', 'Manti', 'Gurtik', 'Quwirdaq']

# Awqatlar dizimin shigariw
print("Awqatlar:", awqatlar)

# Paydalaniwshidan awqat tanlatiw
san = int(input("Bugin ne jeymiz?: "))

# Tanlangan awqatti ulken hariplerde shigariw
print(awqatlar[san - 1].upper())

#7-tapsirma
# 5 isimnen ibarat list jaratiw
isimler = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# Listti shigariw
print(isimler)

# Eki indeks soraw
birinshi = int(input("Birinshi index: "))
ekinshi = int(input("Ekinshi index: "))

# Eki elementtin ornin almastiriw
isimler[birinshi], isimler[ekinshi] = isimler[ekinshi], isimler[birinshi]

# Natijeni shigariw
print(isimler)

#8-tapsirma
# 5 isim hám 5 telefon nomerin saqlaw
isimler = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
telefonlar = ['111', '222', '333', '444', '555']

# Listlerdi shigariw
print("Isimler:", isimler)
print("Telefonlar:", telefonlar)

# Paydalaniwshidan indeks soraw
index = int(input("Index: "))

# Tanlangan isim hám telefon nomerin shigariw
print(isimler[index], ":", telefonlar[index])


#9-tapsirma
# 4 rennen ibarat list jaratiw
renler = ['red', 'yellow', 'green', 'black']

# Renlerdi shigariw
print(renler)

# Ozgertiletuǵin rendin indeksin soraw
index = int(input("Qaysi rendi ozgertiw kerek?: "))

# Jana ren kirgiziw
jana_ren = input("Jana ren kiriting: ")

# Rendi ozgertiw
renler[index - 1] = jana_ren

# Natijeni shigariw
print(renler)

