# Liste in einen String umwandeln

students = ["Max",  "Monika", "Erik", "Franziska"]

# seperator etwas bestimmtest zwischen Elementen hinzufuegen
# was soll hinzugefuegt werden? #, Elemente hintereinander angehaengt werden durch .join() und was soll angehaengt werden? die Liste Students
print("#".join(students))

# Das Ergebnis sieht so aus: Max#Monika#Erik#Franziska
# wenn man nun ein Kommata zwischen den einzelnen Elementen haben moechte, dann einfach die # mit , austauschen

# Ergebnis kann auch in eine Variable gespeichert werden
students_as_string = ", ".join(students)

#Ausgabe
print("An unserer Uni studieren:" + students_as_string)

#String in eine Liste umwandeln
#Zerteilen eines Strings welcher dann zu einer Liste wird

i = "Max, Monika, Erik, Franziska"
#getrennt wird mit .split (wo getrennt wird, wird mit " " bestimmt
print(i.split(", "))

#anderes Beispiel

s = "Ich bin ein Satz mit vielen Woertern"
print(s.split(" "))
#wie viele Elemente in der Liste?
print(len(s.split(" ")))
