#Kontrollstruktueren koennen sein:
# if, else
# Vergleichsoperatoren comparison operatores
# pruefen ob ein Element in einer Liste ist
# else if
# while loop and for loop
# break and continue (zum auswaehlen wer zum Beispiel in einer Liste eine Mail bekommt und wer nicht)

# if else , else if

n = 13
# Einrueckungen sind wichtig, denn sonst gehoert eine Zeile ggf. nicht mehr zur Kontrollstruktur
if n < 42:
    print("Die Zahl ist kleiner als 42")

#Beispiel

m = 10

if m < 5:
    print("m ist kleiner als 5")
else:
    print("ist nicht der Fall")


#booleans (and und or)
#Abfrage zum Beispiel ob eine Person in ihren 30ern ist oder nicht

age = 30

if age >= 30:
    if age <= 39:
        print("Diese Person ist in ihren 30-ern")

# das gleiche kann man auch anders schreiben und kuerzer

if age >= 30 and age <= 39:
    print("Diese Person ist in ihren 30-ern")

# or

if age <= 30 or age > 39:
    print("Diese Person ist nicht in ihren 30-ern")


#boolean

o = True
print(o)
#Ergebnis: True
o = False
print(o)
#Ergebnis: False

#zwischenspeichern von True oder False
age = 25
above_30 = age >= 30
print(above_30)
#Ergebnis: False

#Altertest fuer zum Beispiel Ueberpruefung fuer Alkohol

country = "US"
age = 20

if (country == "US" and age >= 21) or (country != "US" and age >= 18):
    print("Diese Person darf Alkohol trinken")
else:
    print("Diese Person darf keinen Alkohol trinken")
#Ergebnis waere das die Person keinen Alkohol trinken darf weil keiner der beiden Bedingungen erfuellt wurden

# der not operator
age = 25

if not age >= 30:
    print("ausgefuehrt")
# der not operator dreht das Ergebnis einmal um, sprich bei der if Abfrage waere es False aber durch not wird es True
# weiteres Beispiel

names = ["Max", "Nadine"]

if "Moritz" not in names:
    print("Moritz ist nicht ind er Liste enthalten")



