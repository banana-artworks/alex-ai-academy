# 🗄️ Lektion: Datenbanken für deine Python-Lagerverwaltung

**Level 1 | Geschätzte Lernzeit: 15 Minuten**

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:

- ✅ Erklären, was SQLite ist und warum es ideal für Anfänger ist
- ✅ Eine SQLite-Datenbank in Python erstellen
- ✅ Daten einfügen und abfragen
- ✅ Entscheiden, wann SQLite die richtige Wahl ist

---

## 1️⃣ Was ist eine Datenbank?

Stell dir eine Datenbank wie eine **digitale Tabellenkartei** vor:

```
📦 Lager
 ├── Produkt: Schrauben  | Menge: 500 | Preis: 2,99 €
 ├── Produkt: Muttern    | Menge: 200 | Preis: 1,49 €
 └── Produkt: Dübel      | Menge: 150 | Preis: 3,99 €
```

Anstatt Daten in einer Excel-Datei zu speichern, nutzt du eine Datenbank –
das ist **schneller, sicherer und professioneller**.

---

## 2️⃣ Welche Datenbank soll ich nehmen?

Für Anfänger gibt es eine klare Empfehlung:

> ### 🏆 Nimm SQLite!

Hier siehst du, warum:

| Datenbank | Bewertung | Geeignet für Anfänger? |
|-----------|-----------|------------------------|
| **SQLite** | ⭐⭐⭐⭐⭐ | ✅ Ja – perfekt! |
| MySQL | ⭐⭐⭐ | ⚠️ Eher für Teams & Web-Apps |
| MongoDB | ⭐⭐ | ❌ Zu komplex für den Start |
| Excel | ⭐ | ❌ Keine echte Datenbank |

---

## 3️⃣ Was macht SQLite so besonders?

SQLite ist eine **dateibasierte Datenbank** – das bedeutet:

```
Deine gesamte Datenbank = eine einzige Datei
                          📄 lager.db
```

Das bringt dir diese Vorteile:

| Vorteil | Was das bedeutet |
|---------|-----------------|
| 🖥️ **Kein Server nötig** | Läuft direkt auf deinem PC |
| 📦 **Bereits in Python enthalten** | Kein `pip install` nötig! |
| ⚡ **In 5 Minuten startklar** | Sofort loslegen |
| 💰 **Kostenlos** | 100% gratis |
| 💾 **Eine Datei** | Backup = einfach kopieren |

---

## 4️⃣ Dein erstes SQLite-Programm

Gehen wir Schritt für Schritt vor:

### Schritt 1 – Verbindung herstellen

```python
import sqlite3  # ← Bereits in Python eingebaut!

# Verbindung herstellen
# Tipp: Die Datei "lager.db" wird automatisch erstellt,
#       falls sie noch nicht existiert.
conn = sqlite3.connect("lager.db")
cursor = conn.cursor()
```

### Schritt 2 – Tabelle erstellen

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produkte (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,  -- Eindeutige Nummer
        name   TEXT    NOT NULL,                   -- Produktname
        menge  INTEGER NOT NULL,                   -- Lagerbestand
        preis  REAL    NOT NULL                    -- Preis in Euro
    )
""")
```

> 💡 **`IF NOT EXISTS`** sorgt dafür, dass die Tabelle nur einmal erstellt wird –
> du kannst das Programm also beliebig oft starten.

### Schritt 3 – Daten einfügen

```python
# Produkt zur Datenbank hinzufügen
cursor.execute(
    "INSERT INTO produkte (name, menge, preis) VALUES (?, ?, ?)",
    ("Schrauben", 500, 2.99)  # ← Deine Produktdaten
)
```

> 💡 **Warum `?` statt direkter Werte?**
> Die Fragezeichen schützen deine Datenbank vor Fehlern und Angriffen.
> Das nennt sich **Prepared Statement** – merke dir diesen Begriff!

### Schritt 4 – Daten abfragen

```python
# Alle Produkte anzeigen
cursor.execute("SELECT * FROM produkte")
produkte = cursor.fetchall()

for produkt in produkte:
    print(produkt)

# Ausgabe:
# (1, 'Schrauben', 500, 2.99)
```

### Schritt 5 – Speichern und beenden

```python
conn.commit()   # ← Änderungen dauerhaft speichern
conn.close()    # ← Verbindung sauber schließen
```

> ⚠️ **Wichtig:** Vergisst du `conn.commit()`, gehen deine Daten verloren!

---

## 5️⃣ Alles zusammen – das komplette Beispiel

```python
import sqlite3

# Verbindung herstellen
conn = sqlite3.connect("lager.db")
cursor = conn.cursor()

# Tabelle erst