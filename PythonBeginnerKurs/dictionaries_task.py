name_dictionary = {}
name_list = []
max_occurences = 0
name_with_max_occurences = ""
# occurence - Auftreten
with open ("names.csv", "r") as file:
    for line in file:
        data = line.strip().split(",")
        # trenne beim Zeichen , und fuege die Liste jedes mal der Variablen data hinzu
        if data[0] == "Id":
            continue
            # wollen erstmal den Zeilenkopf mit Id, Name usw. ueberspringen daher die if Abfrage
        name = data[1]
        count = int(data[5])
        # fuegen den Variablen den jeweiligen Wert hinzu
        if name in name_dictionary:
        # falls name in Dict vorhanden dann bitte aktuellen count mit dem neuen count addieren
        # bei count muss int() gecastet werden denn sonst werden strings miteinander addiert
        # wollen aber numerische addition
            name_dictionary[name] = name_dictionary[name] + count
        else:
        # falls name noch nicht in Dict dann bitte hinzufuegen mit aktuellen Wert und Anzahl
            name_dictionary[name] = count
    for key, value in name_dictionary.items():
        # schluessel das dict name_dictionary mit .items() in eine art Liste auf und iteriere durch jedes element (tupel)
        if max_occurences < value:
            # WENN max_occurences kleiner als aktueller Wert der iterriert wird dann ersetzen
            max_occurences = value
            # aktuellen key bitte in variable einsetzen
            name_with_max_occurences = key

    print(name_with_max_occurences,max_occurences)

