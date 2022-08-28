__all__ = ["module"]    # schreiben __all__ um die * schreibweise zu erlauben
                        # module ist der Dateiname OHNE .py
                        # nun kann man schreiben from module_test import *
                        # => module.f() funktioniert nun da wir es hier in der init datei mit __all__ definiert haben

# reference 1))
from . import module
# aus dem aktuellen module, importiere die Datei "name datei"