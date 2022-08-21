student1 = "Max"
student2 = "Monika"
student3 = "Erik"
student4 = "Franziska"

students = ["Max", "Monika", "Erik", "Franziska"]
print(students)

# hinzufuegen von neuen Studenten mit .append in die bereits bestehende Liste

students.append("Moritz")

print(students)

# wie viele Eintraege sind in der Liste mit len (len ist eine Funtktion)

print(len(students))

# to print the last item in a list use [-1]
print(students[-1])

# mehrere strings ausgeben lassen

print(students[0] + ' & ' + students[-1])

# einen bestimmten Eintrag in deiner Liste entfernen
# mit del kann man einen Eintrag mit einem bestimmten Index entfernen

students = ["Max", "Monika", "Erik", "Franziska"]
print(students[3])
del students[3]
print(students)

#entfernen ohne Index mit .remove() wenn man genau weiss was entfernt werden soll
students.remove("Monika")
print(students)

# das letzte Element ausgeben mit [-1]
students = ["Max", "Monika", "Erik", "Franziska"]

# List Slicing
print(students[:]) # mit [:] erstellt man eine Kopie mit von einer Liste

print(students[1:]) # [1:] ueberspringt das Element an Stelle 1 und gibt alle anderen an
# Ausgabe: ['Monika', 'Erik', 'Franziska']

print(students[1:-1]) # Ab Index 1 und ausschliesslich dem letzten Element alle ausgeben
# Ausgabe: ['Monika', 'Erik']

print(students[:-1]) # alle Elemente ausschliesslich dem letzten aus der Liste
# Ausgabe: ['Max', 'Monika', 'Erik']

# List Slicing funktioniert auch fuer Strings
print("Hallo Welt"[0:5])
# Ausgabe: Hallo
print("Hallo Welt"[-4:]) # gebe mir die letzten 4 Zeichen aus
# Ausgabe: Welt

# Slicing wird iniziert mit [:] - vor dem : wo moechte ich anfangen
#                               - nach dem : wo soll ich aufhoeren

# Beispiel:
print("Hallo Welt"[6:-1])
# Ausgabe: Welt -> Starte nach der Stelle 6, also hier W und hoere auf bei letztem Element hier also t was mit gehoert

# List comprehension
# Syntax: newlist = [expression for item in iterable if condition == True]
# if statement can be added if needed but can also be left out
xs = [1,2,3,4,5,6,7,8]
# normally we would write something like this:
# ys = []
# for x in ys:
#     ys.append(x)
# with List comprehension we can make it shorter
ys = [x * x for x in xs]
print(ys)
# Ausgabe: [1, 4, 9, 16, 25, 36, 49, 64]
# what it does: creates a list, variable is decleared in the beginning and iterate though list while using for loop
# another Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]
# create a list, iterate through list 'fruits'and check if a in x
print(new_list)
# Ausgabe: ['apple', 'banana', 'mango']

