import pandas as pd

# Vorbereitung
# 1. Suchen und ersetzen: nicht decodierbares e bei Andre
# 2. zweite "Person" Spalte in "Person1" umbenennen (lässt sich besser referenzieren)

# Einlesen der .CSV Datei
dienstplan = pd.read_csv("20220306 Dienstplan-2022.csv", sep=";")


# Dictionary, um Monatsnamen in Monatsnummern umzuwandeln
monate = {"Januar": 1, "Februar": 2, "Maerz": 3, "April": 4, "Mai": 5, "Juni": 6, \
    "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12}
dienstplan["Monat"] = dienstplan["Monat"].replace(monate)

# Sinnvollere Dienstbezeichnungen für die Kalendereinträge
dienstbezeichnungen = {"Fluglehrer": "Fluglehrerdienst", "Flugleiter": "Flugleiterdienst", \
    "Windenfahrer": "Windendienst", "Windenausbilder": "Windendienst", "Kantine": "Kantinendienst"}
dienstplan["Dienst"] = dienstplan["Dienst"].replace(dienstbezeichnungen)

# Zusammenführen der Spalten für Tag,Monat,Jahr in neuer Spalte "Date"
dienstplan["Date"] = pd.to_datetime(dienstplan["Jahr"].astype(str) + "/" + dienstplan["Monat"].astype(str) + "/" + dienstplan["Tag"].astype(str))

# Erstellen einer Namensliste aller Diensthabenden
names = pd.concat([dienstplan["Person"], dienstplan["Person1"]],ignore_index=True).drop_duplicates().dropna().reset_index(drop=True)

# Zusammenführen der beiden Namensspalten. Es wird später nur das Vorkommen des jeweiligen Mitglieds innerhalb der Spalte abgefragt
dienstplan['Person1'].fillna('keiner', inplace=True)
dienstplan['Personen'] = dienstplan['Person'] + " ; " + dienstplan['Person1']

# Schreibe Dienstplan in zwischen-CSV, zu validierungszwecken
dienstplan[["Date", "Dienst", "Personen"]].to_csv("./dp_aufbereitet.csv")
names.to_csv("./namensliste.csv")