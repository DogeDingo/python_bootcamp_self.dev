# while Schleife
# syntax: while (condition):
counter = 0

while counter < 10:
    print(counter)
    countter = counter + 1

# die Bedingung der Schleife steht nach dem while
# ein Zaehler muss nach jeder iteration um eins erhoeht werden
# sonst laeuft die Schleife unendlich lang

# for schleife
# syntax: for (variable) in (condition where to loop through):

for i in range(0,10):
    print(i)

# stelle mir eine Variable i zur Verfuegung die durch den Zahlenbereich 0 bis 10 durchgeht

liste = [5, 8, 10]
for i in liste:
    print(i)

# wenn man weiss wie viele Zahlen man durchgehen muss, dann lieber eine for schleife nutzen
