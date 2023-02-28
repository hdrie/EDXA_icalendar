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
+ Die Kalenderdateien werden in einen Unterordner, hier *./cal/*, geschrieben. Der muss vorher im Arbeitsverzeichnis erstellt worden sein

## Bedienung

**Erfahrung mit Python vorausgesetzt**

1. Beschaffen einer .csv-Datei mit dem Dienstplan, darin manuell die Anpassungen vornehmen, wie in *einlesen.py* kommentiert.
2. Installieren der notwendigen Bibliotheken.
3. Ausführen des Python-Skripts *einlesen.py*. Dabei Pfad und Name der .csv-Datei beachten und ggf im Skript anpassen.
4. Es werden eine optimierte Version des Dienstplans und eine Namensliste erstellt
5. Das Unterverzeichnis *./cal/* erstellen, bzw. ggf. selbst definieren.
6. Ausführen des Python-Skrips *kalender_gen.py*. 
7. Das Tool sollte für jeden Namen in der Namensliste eine *.ics* Datei erstellen. Zusätztlich wird eine Datei mit allen Flugbetriebstagen erstellt.
