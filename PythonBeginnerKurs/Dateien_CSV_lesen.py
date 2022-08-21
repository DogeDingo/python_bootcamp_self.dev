with open("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        # mit strip() entferne Leerzeichen links und rechts,
        # mit split() am Zeichen ; zerlegen und Liste erstellen
        print(data[0] + ": " + data[1])
        # mit dem Index laesst sich einfach steuern, da wir hier in Tabellen denken
        # mit continue ueberspringt man einen ganzen Schleifen durchgang
        if int(data[1]) >= 2000000:
            print(data)




