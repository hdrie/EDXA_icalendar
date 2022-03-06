# EDXA_icalendar
+ Tool zum Erstellen von Kalenderdateien aus einem Dienstplan
+ Geschrieben in python. Die *.ipynb* Dateien lassen sich genau so gut als Python Skripte ausführen


## Erläuterungen zu den Dateien:

*einlesen.ipynb* 
+ iest die CSV-Version des Dienstplans und erstellt eine praktikabler formatierte Zwischenversion und eine Namensliste aller Mitglieder.
+ Der Pfad der Ursprungsdatei muss in hier ggf angepasst werden


*icalendar.ipynb*
+ erstellt je Mitglied in der Namensliste eine *.ics* - Datei
+ Die Kalenderdateien werden in einen Unterordner, hier *./cal1/*, geschrieben. Der muss vorher im Arbeitsverzeichnis erstellt worden sein
