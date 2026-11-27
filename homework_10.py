
Tapsirma-10
#1.Usi sozdin 1 ham 4shi haribin aliw
soz = "Qaraqalpaqstan"

print("0-index:", soz[0])
print("4-index:", soz[4])

#2. Aqirgi ham aqirindagi 3shi haripti aliw
qala = "Tashkent"

print("Sońǵı hárip:", qala[-1])
print("Sońǵıdan úshinshi hárip:", qala[-3])

#3. Birinshi ham aqirgi haripti biriktiriw
til = "Python"

nátiyje = til[0] + til[-1]

print(nátiyje)

#4. Qant bahasin esaplaw
words = "Qumsheker 12000 sum"

at = input("Atıńız: ")

kg = int(input("Neshe kg qant kerek? "))

baha = int(words[10:15])

jámi = kg * baha

print("=" * 20)
print("Xaridar:", at, "(Háripler sani:", len(at), ")")
print("Tólew muǵdarı:", jámi, "sum")
print("=" * 20)
