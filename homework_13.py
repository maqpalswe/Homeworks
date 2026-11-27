

#Homework-13
#1-tapsrma
word = "programming"

# 2-indeksten baslap sózdi bóliw
natija = word[2:]

# Barlıq háriplerdi úlken qılıw
print(natija.upper())

#2-tapsirma
text = "PYTHON PROGRAMMING"

# Dáslepki 5 háripti ajıratıw
natija = text[:5]

# Kishi háriplerde shıǵarıw
print(natija.lower())

#3-tapsirma
text = "salem-dostim-python"

# Sızıqsmanı bos orın menen almastırıw
text = text.replace("-", " ")

# Hár bir sózdiń birinshi háripin úlken qılıw
print(text.title())

#4-tapsirma
text = "men python uyren...men"

# Aqırǵı sózdi ajıratıp alıw
soz = text.split()[-1]

# Birinshi háripin úlken qılıw
print(soz.capitalize())

#5-tapsirma 
name = "ali"

# Attı úlken háriplerge ózgertiw
print(f"Salam, {name.upper()}! PYTHONGA XOSH KELIPSIZ!")

#6-tapsirma
text = "Qaraqalpaqstan"

# a háribiniń sanın anıqlaw
soni = text.count("a")

# Nátiyjeni shıǵarıw
print(soni)

#7-tapsirma
text = "Python PROGRAMMING pYTHON"

# Barlıq háriplerdi kishi qılıw
text = text.lower()

# p háribiniń sanın anıqlaw
soni = text.count("p")

print(soni)

#8-tapsirma
text = "Qaraqalpaqstan"

# Aqırǵı háriptiń indeksin tabıw
indeks = len(text) - 1

print(indeks)

#9-tapsirma
number = "1020304050"

# Barlıq 0 sanların 5 ke almastırıw
natija = number.replace("0", "5")

print(natija)

#10-tapsirma
text = "men python tilin jaqsi koremen"

# Python sózin JAVA menen almastırıw
text = text.replace("python", "JAVA")

# Barlıq háriplerdi úlken qılıw
print(text.upper())

#11-tapsirma
text = "    Python dasturlash    "

# Basındaǵı hám aqırındaǵı bos orınlardı alıp taslaw
print(text.strip())

#12.
text = "    Salom Dunyo    "

# Tek shep táreptegi bos orınlardı alıp taslaw
print(text.lstrip())

$13.
text = "    Salom Dunyo    "

# Tek oń táreptegi bos orınlardı alıp taslaw
print(text.rstrip())


#14.
text = "    qaraqalpaqstan jaslari    "

# Artyqsha bos orınlardı alıp taslaw
text = text.strip()

# Hár bir sózdiń birinshi háripin úlken qılıw
print(text.title())

#15.
# At hám familiyanı kirgiziw
name = input("Atıńız hám familiyańızdı kirgiziń: ")

# Bos orınlardı alıp taslaw hám háriplerdi durıslaw
name = name.strip().title()

# Nátiyjeni shıǵarıw
print(f"Salem, {name}!")
print("Xosh kelipsiz!")

#16.
name = "Muhammad"

# Birinshi 3 háripti ajıratıp alıw
natija = name[:3]

# Úlken háriplerge ózgertiw
print(f"Sizdiń kodingiz: {natija.upper()}")

#17.
text = "Qaraqalpaqstan"

# a háribiniń sanın esaplaw
a_sani = text.count("a")

# o háribiniń sanın esaplaw
o_sani = text.count("o")

# Nátiyjeni shıǵarıw
print(f"a hárifi: {a_sani} márte")
print(f"o hárifi: {o_sani} márte")

#18.
email = "student@gmail.com"

# @ belgisi indeksin tabıw
indeks = email.index("@")

# @ belgisineniń aldındaǵı sózdi ajıratıw
natija = email[:indeks]

print(natija)

#19.
text = "Python Programming"

print(text.index("Java"))
text = "Python Programming"

# Java sózi tekstte bolmaǵanı ushın index() qáte beredi
# find() sóz tabılmasa -1 nátiyjesin qaytaradı
print(text.find("Java"))


#20.
word = "banana"

# z háripi sózde bolmaǵanı ushın rindex() qáte beredi
# find() hárip tabılmasa -1 qaytaradı
print(word.find("z"))

#21.
text = "    python_programming_language    "

# Basındaǵı hám aqırındaǵı bos orınlardı alıp taslaw
text = text.strip()

# _ belgisin bos orın menen almastırıw
text = text.replace("_", " ")

# Hár bir sózdiń birinshi háripin úlken qılıw
print(text.title())

#22.
text = "    qaraqalpaqstan-python-tili    "

# Artyqsha bos orınlardı alıp taslaw
text = text.strip()

# Sızıqsmanı bos orın menen almastırıw
text = text.replace("-", " ")

# Hár bir sózdiń birinshi háripin úlken qılıw
text = text.title()

# a háribiniń neshe márte qatnasqanın anıqlaw
a_sani = text.count("a")

# Birinshi bos orınnıń indeksin tabıw
indeks = text.index(" ")

# Barlıq nátiyjelerdi ekranǵa shıǵarıw
print(f"Matn: {text}")
print(f"A hárifi: {a_sani} márte")
print(f"Birinshi bos orın indeksi: {indeks}")
