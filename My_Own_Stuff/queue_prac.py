import queue

q = queue.Queue()

# mit .put koennen wir etwas einer Queue hinzufuegen
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

# als Rueckgabe erhalten wir ein Objekt
print(q)

# um auf ein Element zuzugreifen
# mit der .get() Methode
print(q.get())
# einmal ausgefuehrt wird das erste Element was der Queue hinzugefuegt wurde entnommen

# eine Schleife mit Queue sieht wie folgt aus:
# while not q.empty():
#     element = q.get()
#     print(element)

q = queue.PriorityQueue()

q.put((10, "hallo welt"))
q.put((15, "mars"))
q.put((5, "wichtig"))

print(q.get())
print(q.get())

text = "A A A A A A A A B B B B B B B B B B C C C C C D D D E E E E E E"
d = {}
for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(d)

# um Zugriff auf ein Tupel zu erhalten muss man folgendes schreiben
test_tuple = (10, "March")
a, b = (test_tuple)
print(a, b)
# Ausgabe: 10 March

pq = queue.PriorityQueue()
for word, number in d.items():
    # die .items() methode wandelt ein Dictionary in eine Liste mit Tupeln um
    # daher in Zeile 53 die Schreibweise (-number, word) da wir auf ein Tupel zugreifen moechten
    pq.put((-number, word))
    # das Minus - vor number dreht die Reihenfolge um in der die PQ ausgegeben wird. Vom hoechsten zum niedrigsten
    # andersheraum dann einfach das Minuszeichen weglassen
print(pq.get())


