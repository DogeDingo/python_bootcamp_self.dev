# Dictionaries in Python
# - Du kannst Wertezuordnungen speichern (z.B. Telefonbuch: Ein Nachname hat eine Telefonnummer)
# - Du kannst nachtraeglich Elemente veraendern / entfernen / hinzufuegen
# - Dictionaries brauchst du wirklich immer wieder

# dictionaries haben Key und Value
# KEY: VALUE
# ein Key ist sozusagen mit einem Value verbunden und das geschieht mit : collon
d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print(d)
# Ausgabe:{'Berin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN'}
print(d["Helsinki"])
# mit einem Index [] und dem Stringnamen kann man auf den Key zugreifen und die Value erhalten
# ueberprueft ob ein Wert dem Eintrag Helsinki zugeordnet ist
# Ausgabe: HEL

# hinzufuegen von einem Eintrag
d["Budapest"] = "BUD"
print(d)
# Ausgabe:{'Berin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN', 'Budapest': 'BUD'}

# entfernen eines Eintrags
del d["Budapest"]
print(d)
# Ausgabe: {'Berin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN'}
# entfernt also Eintrag sowie zugeordneten Wert BUD

# Abfrage: Ist ein Element im Dictionary?
if "Budapest" in d:
    print("Budapest ist im Dictionary enthalten")
if "Saigon"in d:
    print("Saigon ist im Dictionary enthalten")
# Ausgabe: "Saigon ist im Dictionary enthalten"

# Auf ein Element zugreifen:
print(d["Saigon"])
print(d.get("Saigon"))
# Ausgabe: beide SGN
# tendenziell aber lieber [] nutzen als .get() da Programm dann abbricht und besser fuer bug report

# Dictionary and loops

d = {"Muenchen": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

for key in d:
    value = d[key]
    print(key)
    print(value)

# Ausgabe
# Muenchen
# MUC
# Budapest
# BUD
# Helsinki
# HEL

# Alle Werte im Dictionary als eine Art Liste ausgeben lassen mit Tupel

print(d.items())
# Ausgabe
# dict_items([('Muenchen', 'MUC'), ('Budapest', 'BUD'), ('Helsinki', 'HEL')])
# Das ist jedoch keine richtige Liste!!

for key,value in d.items():
    print(key + ": " + value)

# Ausgabe
# Muenchen: MUC
# Budapest: BUD
# Helsinki: HEL
