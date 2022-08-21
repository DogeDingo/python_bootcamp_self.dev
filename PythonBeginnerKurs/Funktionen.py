# Funktion

def multi_print(name):
    print(name)
    print(name)

multi_print("HALLO")
multi_print("WELT")

def multi_counter(name, count):
    for i in range(1, count):
        print(name)

multi_counter("Hallo", 5)

# Funktionen koennen Funktionen beinhalten

def multi_function():
    multi_counter("Hallo", 3)
    multi_counter("Welt", 3)

multi_function()

# return um weiter mit Ergebnis zu arbeiten
# Rueckgabewert

def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(1,5)
print(result)

