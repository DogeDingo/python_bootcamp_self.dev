# wir importieren das Module aus dem Ordner module_test

from module_test import module
# module_test mit nur einen Teil geladen und zwar der Datei module
module.f()

# nun moechte ich aber den ganzen Ordner
import module_test
# funktioniert so erst nicht, man muss noch was in der __init__ datei was aendern
# reference 1))

module_test.module.f()
# Syntax: moduleordner_name.datei_name.funktion_name()

import sys
print(sys.version)

import csv
# csv - comma seperated values
with open("datei.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=";")
    # delimiter ist das Trennzeichen aus der Datei
    # es gibt noch quotechar='(Zeichen welches einen Eintrag ummantelt)'
    # zB kann ein Eintrag in einer CSV Datei als "Hallo;Welt"stehen was gleich dem delimiter ist
    # das heisst man muss nun noch Python sagen, dass Zeichen " einen Eintrag beinhaltet
    # wuerde dann so aussehen: quotechar='"'
    for line in csv_file:
        print(line)
