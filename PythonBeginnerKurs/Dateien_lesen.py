with open("lesen.txt", "r") as f:
    for line in f:
        # da ausgabe "String\n" ist, kann man mit .strip() das \n entfernen um keine freie leere Zeile zu erhalten
        print(line.strip())

#context manager: with open(<name file>, MODE) as variable:
with open("schreiben.txt", "w") as f:
    f.write("asdfasdf\n")
    f.write("Frage1")

# mit w wird immer ueberschrieben und mit a (fuer append) werden Dinge immer hinten rangehaengt