# Tupel
# Mutable (veraenderlich) vs Immutable (unveraenderlich)
# Liste: Veraenderliche Datenstruktur
# Tupel: Unveraenderliche Datenstruktur

person = ("Max Bauer", 55)

# ein Tupel entpacken

students = ("Franky", 29, "Cyborg")
# Anzahl der Elemente muss dem des Tupels entsprechen
name, age, specialty = students
print(name, age, specialty)

# einige Beispiele fuer Tupel

def get_student():
    return("MaxiKing", 22, "Candy")
# Ausgabe ist ein Tupel welches dann entpackt wird
name, age, sweets = get_student()
print(name)
print(age)
print(sweets)

# weiteres Beispiel

# liste mit Tupels
students = [
    ("Franky", 29), # das , nicht vergessen
    ("MaxiKing", 23)
]
# mit einer For Schleife direkt das Tupel entpacken

for name, age in students:
    print(name)
    print(age)

