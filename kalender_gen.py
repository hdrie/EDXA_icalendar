import icalendar as ic
import datetime as dt
import pytz
import pandas as pd


# Definieren einer Dienst-Klasse mit den wichtigsten Attributen.
# Der Name der Person taucht nicht auf, da die Dienste später je Mitglied in einer eigenen Liste gesammelt werden
class Dienst:
    def __init__(self, typ, datum):
        self.type = typ # Art des Dienstes: Fluglehrer, Flugleiter, Windenfahrer, Kantine
        self.date = datum
        if self.date.weekday() == 5: # Abfrage, ob der Tag ein Samstag ist; Definition der Dienstzeiten (Lokalzeit)
            self.tstart = dt.datetime.combine(self.date, dt.time(13,0,0,0))
            self.tend = dt.datetime.combine(self.date, dt.time(18,0,0,0))
        else:
            self.tstart = dt.datetime.combine(self.date, dt.time(10,0,0,0))
            self.tend = dt.datetime.combine(self.date, dt.time(18,0,0,0))

# Funktion zum Konvertieren der Lokalzeit in UTC unter Berücksichtigung der Zeitumstellung
def local_to_utc(_dt, _tz='Europe/Berlin'):
    timezone=pytz.timezone(_tz)
    utc=pytz.utc
    return timezone.localize(_dt).astimezone(utc)

# Funktion zum generieren eines icalendar-Kalenders, nimmt eine Liste von Dienst-Objekten an
def gen_calendar(dienste):
    cal = ic.Calendar()
    cal.add('prodid', '-//Dienstplan_Achmer//von_hauken.com//')
    cal.add('version', '2.0')
    cal.add('calscale', 'GREGORIAN')
    cal.add('method', 'PUBLISH')

    events = {} # Generieren der einzelnen Termine innerhalb des Kalenders. Nutzen eines Dicts, um fortlaufend Events zu benennen und zu hinterlegen
    for i,n in enumerate(dienste):
        events[f"event{i}"] = ic.Event()
        events[f"event{i}"].add("uid", f"Achmer-Dienst-{n.date.isoformat()}")
        events[f"event{i}"].add("summary", f'{n.type} Achmer') # Name, der später im Kalender angezeigt wird
        events[f"event{i}"].add("dtstart", local_to_utc(n.tstart)) # Startzeit, als datetime-objekt
        events[f"event{i}"].add("dtend", local_to_utc(n.tend)) # Endzeit
        events[f"event{i}"].add("dtstamp", dt.datetime.now(dt.timezone.utc)) # Zeitstempel der Erstellung
        events[f"event{i}"].add("status", "CONFIRMED")
        cal.add_component(events[f"event{i}"])
    return cal # Rückgabe des Kalenders

# Funktion zum schreiben des übergebenen Kalenders in eine .ics Datei. Der Name der betreffenden Person wird zum Dateinamen
def write_calendar(name, cal):
    with open(f"./cal/{name}.ics", "wb") as f: # "wb": Die .to_ical()-Funktion gibt einen b''-String (binary) raus, daher write-binary
        f.write(cal.to_ical())

# Einlesen der vorbereiteten Datenbanken
names = pd.read_csv("./namensliste.csv")
names = names['0'].tolist() # Vereinfachung der Namensliste als einfache liste
dienstplan = pd.read_csv("./dp_aufbereitet.csv")

# Je Mitglied in der Namensliste Erstellung einer Kalenderdatei
for mitglied in names:
    diensttage = dienstplan[dienstplan['Personen'].str.contains(mitglied)] # Filterung nach Zeilen, in dem das Mitglied vorkommt, also einen Dienst hat
    dienste = []

    for index, row in diensttage.iterrows(): # Sukzessive Erstellung von Dienst-Objekten und Sammlung in einer Liste 
        dienste.append(Dienst(row['Dienst'], dt.date.fromisoformat(row['Date'])))

    cal = gen_calendar(dienste) # Generieren des Kalenders
    write_calendar(mitglied, cal) # Schreiben des Kalenders
