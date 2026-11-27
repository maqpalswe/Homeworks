
Tapsirma-9
#1. Paydalaniwshiin atim ham familiyasin biriqtirw
ism = input("Ismingiz: ")
familiya = input("Familiyangiz: ")

tolik_ism = ism + " " + familiya

print("To'liq ism:", tolik_ism)

#2. Sozdi bir neshe ret takirallaw
soz = input("So'z kiritiń: ")
san = int(input("Neshe márte tákirarlaymız? "))

nátiyje = soz * san

print("Nátiyje:", nátiyje)

#3. At haripteriin sanin aniqlaw
at = input("Atıńızdı kiritiń: ")

print("Sizdiń atıńız", len(at), "ta háripten ibarat.")
#4. Atinda neshe harip bar ekenin aniqlaw
at = input("Atıńızdı kiritiń: ")

print("*" * len(at))
print("Sálem,", at + "!")

#5.Kartoshka bahasin esaplaw
at = input("Atıńız kim? ")

kg = int(input(at + ", neshe kg kartoshka kerek? "))

baha = 5000
jámi = kg * baha

print(at + ",", kg, "kg kartoshka ushın", jámi, "som tóleysiz.")

#7. Atin takirallaw ham harip sanin aniqlaw
at = input("Atıńız: ")

san = int(input("Neshe márte tákirarlaymız? "))

nátiyje = at * san

print("Nátiyje:", nátiyje, "(Háripler sani:", len(at), ")")

#8.Tiwilgan jil boyinsha jasin esaplaw
at = input("Atıńız: ")

tuwılǵan_jıl = int(input("Qaysı jılı tuwılǵansız? "))

jas = 2026 - tuwılǵan_jıl

print(at + ", siz", jas, "jasdasız
