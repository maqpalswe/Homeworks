

#Tapsirmalar-8
# input "str" ham int bolganliqtan qate boladi TypeError
#1. Qateni tabiw
narx = input("Narxni kiriting: ")
umumiy = narx + 500
print(umumiy)
#Duris kod
narx = int(input("Narxni kiriting: "))
umumiy = narx + 500
print(umumiy)

#2. Paydalanuvchining bir oylik ish daromadi uni 12 ga koʻpayitirib bir yillik daromadi

ish_haqqi = int(input("Sizning bir oylik daromadingiz qancha sum? "))
umumiy_narx = ish_haqqi * 12
print(umumiy_narx)

#3.Tomendegi koddagi qateni tabiw
sheker_bahasi = 12000
sheker_kg = 2
jalpi_sum = sheker_bahasi * sheker_kG # tobedegi kodqa qarasaq kg bolip jazilgan kG qate!
print(jalpi_sum)

#4.
alma = 50
satilgan = int(input("Nechta olma sotdingiz? "))
qoldi = alma - satilgan

print("Qutida", qoldi, "ta olma qoldi.")

#5.Paydalaniwshidan neshe biylet kerek ekenin sorae ham jami hahasin esaplaw
baha = 25000
bilet = int(input("Nechta chipta olasiz? "))
jami = baha * bilet

print("Jami to'lov:", jami, "so'm.")

#6. idista 25 mayek bar otbasindagi adam sanina qarap boliw
mayek = 25
odam = int(input("Oila a'zolaringiz soni nechta? "))

har_biriga = mayek // odam
ortib_qoldi = mayek % odam

print("Har biriga:", har_biriga, "tadan")
print("Ortiq qoldi:", ortib_qoldi, "ta")

#7.Neshinshi klasta oqiytinin sorap ham neshe jildan keyin 11-klass bolatinin aytiw
sinf = int(input("Hozir nechanchi sinfda o'qiysiz? "))
yil = 11 - sinf

print("Siz", yil, "yildan keyin maktabni bitirasiz!")

#8. 250 betli kitap oni neshe kunde neshe bettem oqiytinin aniqlaw
kitap = 250
bet = int(input("Bir kunda nechta sahifa o'qiysiz? "))

kun = (kitap + bet - 1) // bet

print("Siz bu kitobni", kun, "kunda o'qib tugatasiz
