

Tapsirma-11
#1-tapsirma
word = "Dasturlash"

print("Birinshi harip:", word[0])
print("Aqirgi harip:", word[-1])
print("Ushinshi harip:", word[2])
print("Aqiridan ekinshi harip:", word[-2])
print("Beshinshi harip:", word[4])

#2-tapsirma
word = "Maktab 9 sinf oquvchilar"

mektep = word[0:6]
san = word[7:8]
klass = word[9:13]
oqiwshilar = word[14:24]

print(mektep)
print(san)
print(klass)
print(oqiwshilar)

3-tapsirma
product = "Samsung Galaxy S25 Ultra"

brand = product[0:7]
model = product[8:14]
versiya = product[15:18]
qosimsha = product[19:24]

print("Brend:", brand)
print("Model:", model)
print("Versiya:", versiya)
print("Qosimsha:", qosimsha)
print("Uliwma belgiler sani:", len(product))

#4-tapsirma
name = input("Atinizdi kirgizin: ")
age = int(input("Jasinizdi kirgizin: "))

# Bul jerde үтир qoyiliwi kerek
print("Salom", name)

# Jasqa 1 qosamiz
next_age = age + 1

print("Keyingi jil jasiniz:", next_age)

#5-tapsirma
waqt = "14:45:30"

saat = waqt[0:2]
minut = waqt[3:5]
sekund = waqt[6:8]

print("Saat:", saat)
print("Daqiqa:", minut)
print("Soniya:", sekund)

#6-tapsirma
num = "67.9 + 100.8"

birinshi = int(float(num[0:4]))
ekinshi = int(float(num[7:12]))

juwap = birinshi + ekinshi

print(birinshi, "+", ekinshi, "=", juwap)

#7-tapsirma
computers = "Kompyuterler: HP, Acer, Lenovo"

jana = computers[::-1]

print(jana)

#8-tapsirma
haripler = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

bas_harip = haripler[0::2]
kishi_harip = haripler[1::2]

print("Bas haripler:", bas_harip)
print("Kishi haripler:", kishi_harip)

#9-tapsirma
card = "8600123456789012"

jasirin = "*" * (len(card) - 4) + card[-4:]

print(jasirin)
