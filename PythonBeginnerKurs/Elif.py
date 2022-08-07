# elif als eine verbindung zwischen else und if
# gut nutzbar wenn man mehrere else und if hat

currency = "€"

if currency == "$":
    print("US-Dollar")
else:
    if currency == "¥":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "฿":
                print("Thai Baht")
# Ausgegeben wird hier Euro
# das ganze kann man aber verkuerzen indem man Elif nutzt

currency = "Euro"

if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Baht")

# ausgegeben wird hier auch Euro
# nur ist uebersichtlicher

