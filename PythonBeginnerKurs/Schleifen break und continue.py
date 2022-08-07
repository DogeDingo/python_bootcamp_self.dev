# continue
# wird genutzt um bestimmte Eintraege zu ueberspringen
# Beispiel:

for i in range(0,10):
    if i == 3:
        continue
    print(i)

# gibt alle Zahlen von 0 bis 9 aus aber ohne die 3
# mit continue haben wir gesagt, dass wenn i == 3 dann ueberspring den print

for i in range(0,10):
    if i == 3:
        break
    print(i)

# abbrechen einer Schleife mit break
# also Ausgabe wird nur 0,1,2 sein

# weiteres Beispiel fuer Break
# Ich habe eine Liste und moechte, dass sobald die Zahl > als 10 ist, die For Schleife abgebrochen wird

liste = [4, 6, 7, 2, 4, 6, 7]

s = 0

for element in liste:
    s = s = element
    if s > 10:
        break

print(s)