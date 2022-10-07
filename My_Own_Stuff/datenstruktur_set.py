# in einem set ist jedes element nur einmal vertreten
# set() Ausgabe jedoch mit geschweiften Klammern
# sets ordnet die Elemente jedoch nicht
# das heisst mit einem Index darauf zugreifen kann zu problemen fuehren

text = "Dies ist ein Text mit tollen Worten"
words = set()

for word in text.split(" "):
    words.add(word)
print(words)
print(len(words))