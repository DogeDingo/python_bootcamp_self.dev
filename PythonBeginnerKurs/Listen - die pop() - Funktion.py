# wie entferne ich das letzte Element einer Liste?
# .pop() funktion entfernt letzten Eintrag

planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun", "Pluto"]
planets.pop()
print(planets)

# .pop() gibt auch etwas zurueck (Rueckgabewert)
planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun", "Pluto"]

p = planets.pop() # letzte Element wird entfernt und in eine Variable gespeichert
print(p)
