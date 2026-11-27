

Homework-12
#1-tapsirma

text = "Men python úyrenip atırman"

# Python sózin English sózi menen almastırıw
text = text.replace("python", "English")

# Barlıq háriplerdi úlken qılıw
print(text.upper())

name = "Ali"
age = 18
city = "Tashkent"

# Mag'lıwmatlardı bir gápke birlestiriw
print(f"Meniń atım {name}. Men {age} jastaman. Men {city} qalasında jasayman.")

#2-tapsirma
name = "Ali"
age = 18
city = "Tashkent"

# Mag'lıwmatlardı bir gápke birlestiriw
print(f"Meniń atım {name}. Men {age} jastaman. Men {city} qalasında jasayman.")

#3-tapsirma
text = "PYTHON PROGRAMMING"

# Barlıq háriplerdi kishi qılıw
print(text.lower())

# Tek birinshi háripti úlken qılıw
print(text.capitalize())

# Hár bir sózdiń birinshi háripin úlken qılıw
print(text.title())

#4-tapsirma
text = "Python is easy. Python is powerful. I love Python."

# Python sóziniń neshe márte qatnasqanın anıqlaw
soni = text.count("Python")

# Nátiyjeni ekranǵa shıǵarıw
print(f"Python sózi {soni} márte qatnasqan.")

#5-tapsirma
product = "laptop"
price = 750.567
quantity = 2

# Ul'ıwma bahasın esaplaw
total = price * quantity

# Tovar haqqında maǵlıwmatlardı shıǵarıw
print(f"Ónim: {product.capitalize()}")
print(f"Bahası: {price:.2f}")
print(f"Sani: {quantity} dana")
print(f"Jámi baha: {total:.2f}")

#6-tapsirma
name = input("Atıńızdı kirgiziń: ")

# Ortadaǵı háriplerdi * belgisi menen almastırıw
result = name[0] + "*" * (len(name) - 2) + name[-1]

# Nátiyjeni shıǵarıw
print("Nátiyje:", result)


#7-tapsirma
ati = "Aziz"
familasi = "Almuratov"
jasi = 28
poshtasi = "aziz@email.com"

# Maǵlıwmatlardı ekranǵa shıǵarıw
print(f"""
   Ati:{ati}
   familasi: {familasi}
   Jasi:{jasi}
   Elektron poshtasi:{poshtasi}
""")

#8-tapsirma
mevalar = ["Alma", "Banan", "Anar", "Júzim"]

# Pайдалanıwshıdan mıywe tańlaw
tanlov = int(input("Qaysı miyweni tańlaysız? "))

# Tańlawdı tekseriw
if 1 <= tanlov <= 4:
    print(f"Siz tańlaǵan miywe: {mevalar[tanlov - 1]}")
else:
    print("Bunday miywe joq!")

#9-tapsirma
mevalar = ["Alma", "Banan", "Anar"]
bahalar = [4, 7, 5]

# Satıp alınatuǵın miyweni tańlaw
tanlov = int(input("Qaysı miyweni satıp alasız? "))

# Miyweniń muǵdarın kirgiziw
kg = int(input("Neshe kg kerek? "))

# Tańlawdı tekseriw
if 1 <= tanlov <= 3 and kg > 0:

    # Tańlanǵan miyweniń atın alıw
    meva = mevalar[tanlov - 1]

    # Miyweniń bahasın alıw
    narx = bahalar[tanlov - 1]

    # Ul'ıwma bahasın esaplaw
    jami = narx * kg

    # Nátiyjeni shıǵarıw
    print(f"{meva} {kg} kg = {jami}$")

else:
    print("Qáte tańlaw!")

 #10-tapsirma
 menu = "1. Burger 25$ 2. Lavash 30$ 3. Hot-dog 15$ 4. Pizza 45$"

taomlar = ["Burger", "Lavash", "Hot-dog", "Pizza"]
bahalar = [25, 30, 15, 45]

# Paydalanıwshıdan taǵam tańlaw
tanlov = int(input("Ne buyırtpa qılasız? "))

# Buyırtpa sanın kirgiziw
soni = int(input("Neshe buyırtpa? "))

# Tańlanǵan taǵamdı anıqlaw
taom = taomlar[tanlov - 1]

# Ulıwma bahasın esaplaw
jami = bahalar[tanlov - 1] * soni

# Nátiyjeni ekranǵa shıǵarıw
print(f"Siz {soni} ta {taom.upper()} buyırtpa qıldıńız.")
print(f"Jámi: {jami}$")
 
#11-tapsirma
kitoblar = ["Python", "English", "Mathematics"]
bahalar = [20, 15, 18]

# Paydalanıwshıdan kitap tańlaw
tanlov = int(input("Qaysı kitaptı alasız? "))

# Kitap sanın kirgiziw
soni = int(input("Neshe kerek? "))

# Tańlanǵan kitaptı anıqlaw
kitob = kitoblar[tanlov - 1]

# Kitap bahasın anıqlaw
narx = bahalar[tanlov - 1]

# Kitap atındaǵı belgiler sanın anıqlaw
belgilar = len(kitob)

# Ulıwma bahasın esaplaw
jami = narx * soni

# Nátiyjelerdi shıǵarıw
print(f"Siz {soni} ta {kitob.upper()} kitabın satıp aldıńız.")
print(f"Kitap atındaǵı belgiler sani: {belgilar}")
print(f"Jámi narx: {jami}$")

#12-tapsirma
mahsulotlar = ["Sut", "Non", "Tuxum", "Pishloq"]
bahalar = [2, 1, 5, 8]

# Birinshi tovardı tańlaw
bir = int(input("Birinshi mahsulottı tańlań: "))

# Birinshi tovardıń muǵdarın kirgiziw
son1 = int(input("Sutdan neshe alasız? "))

# Ekinshi tovardı tańlaw
eki = int(input("Ekinshi mahsulottı tańlań: "))

# Ekinshi tovardıń muǵdarın kirgiziw
son2 = int(input("Pishloqtan neshe alasız? "))

# Tovar atların anıqlaw
at1 = mahsulotlar[bir - 1]
at2 = mahsulotlar[eki - 1]

# Hár bir tovardıń bahasın esaplaw
narx1 = bahalar[bir - 1] * son1
narx2 = bahalar[eki - 1] * son2

# Ulıwma bahasın esaplaw
jami = narx1 + narx2

# Chekti ekranǵa shıǵarıw
print("========== CHEK ==========")

print(f"{at1.upper()}: {son1} ta = {narx1}$")
print(f"{at2.upper()}: {son2} ta = {narx2}$")

print(f"\nJámi tólem: {jami}$")

print("==========================")
