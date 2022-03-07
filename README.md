# EDXA_icalendar
+ Tool zum Erstellen von Kalenderdateien aus einem Dienstplan
+ Geschrieben in Python.


## Bibliotheken:
+ pandas
+ icalendar
+ datetime
+ pytz


## Erläuterungen zu den Dateien:

*einlesen.py* 
+ liest die CSV-Version des Dienstplans und erstellt eine praktikabler formatierte Zwischenversion und eine Namensliste der Diensthabenden.
+ Der Pfad der Ursprungsdatei muss in hier ggf angepasst werden


*kalender_gen.py*
+ erstellt je Mitglied in der Namensliste eine *.ics* - Datei, die in den persönlichen Kalender importiert werden kann. Viele, aber nicht alle Apps und Programme unterstützen den Import von .ics-Dateien
+ Die Kalenderdateien werden in einen Unterordner, hier *./cal1/*, geschrieben. Der muss vorher im Arbeitsverzeichnis erstellt worden sein
