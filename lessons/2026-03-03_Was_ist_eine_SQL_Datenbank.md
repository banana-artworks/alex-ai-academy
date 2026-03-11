# 🗄️ Lektion 1: SQL-Datenbanken – Dein erster Einstieg

**Niveau:** Anfänger (Level 1)
**Dauer:** ca. 10–15 Minuten
**Ziel:** Du verstehst, was eine SQL-Datenbank ist und wofür sie verwendet wird.

---

## 🎯 Was lernst du in dieser Lektion?

- ✅ Was eine Datenbank ist
- ✅ Was SQL bedeutet
- ✅ Wie eine Datenbank aufgebaut ist
- ✅ Die 4 wichtigsten SQL-Befehle
- ✅ Wo SQL im Alltag vorkommt

---

## 📦 Was ist eine Datenbank?

Stell dir einen **digitalen Aktenschrank** vor – ordentlich sortiert, jederzeit durchsuchbar und blitzschnell abrufbar.

> **Definition:** Eine Datenbank ist ein organisierter Speicherort für Daten.

### 💡 Alltagsbeispiel
Genau wie ein Telefonbuch **Namen und Nummern** speichert, speichert eine Datenbank **strukturierte Informationen** – zum Beispiel Kundendaten eines Online-Shops.

---

## 🗣️ Was ist SQL?

**SQL** steht für:

> 🇬🇧 **S**tructured **Q**uery **L**anguage
> 🇩🇪 **Strukturierte Abfragesprache**

SQL ist die **Sprache**, mit der du mit einer Datenbank kommunizierst.

### Mit SQL kannst du Daten …

| Aktion | Bedeutung |
|--------|-----------|
| 📖 **Lesen** | Informationen abrufen |
| ➕ **Hinzufügen** | Neue Einträge speichern |
| ✏️ **Ändern** | Bestehende Daten aktualisieren |
| 🗑️ **Löschen** | Einträge entfernen |

---

## 🏗️ Aufbau einer SQL-Datenbank

Eine Datenbank ist wie eine **Sammlung von Tabellen** – ähnlich wie in Excel.

```
📁 Datenbank: „Onlineshop"
 └── 📋 Tabelle: „Kunden"
      ├── 🏷️ Spalte: Name
      ├── 🏷️ Spalte: E-Mail
      └── 🏷️ Spalte: Stadt
```

### 📊 Die wichtigsten Begriffe auf einen Blick

| Begriff | Erklärung | Beispiel |
|--------|-----------|---------|
| **Datenbank** | Der gesamte Speicher | `Onlineshop` |
| **Tabelle** | Eine Kategorie von Daten | `Kunden` |
| **Spalte** | Eine Eigenschaft | `Name`, `E-Mail` |
| **Zeile** | Ein einzelner Datensatz | Max Mustermann |

### 🖼️ So sieht eine Tabelle aus

| ID | Name | E-Mail | Stadt |
|----|------|--------|-------|
| 1 | Max Mustermann | max@mail.de | Berlin |
| 2 | Anna Schmidt | anna@mail.de | Hamburg |
| 3 | Tom Meier | tom@mail.de | München |

---

## ⌨️ Die 4 wichtigsten SQL-Befehle

Merke dir diese vier Befehle – sie bilden das **Fundament von SQL**:

```sql
SELECT  -- 📖 Daten lesen und abfragen
INSERT  -- ➕ Neue Daten hinzufügen
UPDATE  -- ✏️ Bestehende Daten ändern
DELETE  -- 🗑️ Daten löschen
```

> **👶 Anfänger-Tipp:** Keine Sorge, du musst die Befehle noch nicht anwenden können. In späteren Lektionen übst du jeden Befehl einzeln mit Beispielen!

---

## 🌍 Wo begegnet dir SQL im Alltag?

SQL läuft **unsichtbar im Hintergrund** – fast überall!

| Bereich | Beispiel |
|---------|---------|
| 🛒 Online-Shops | Produkte, Bestellungen, Lagerbestand |
| 👤 Social Media | Nutzerprofile, Beiträge, Freundeslisten |
| 🏦 Banken | Kontodaten, Überweisungen |
| 📱 Apps | Login-Daten, Einstellungen, Verlauf |

---

## 📝 Zusammenfassung

| Was? | Kurz erklärt |
|------|-------------|
| **Datenbank** | Organisierter digitaler Speicher |
| **SQL** | Sprache zur Kommunikation mit der Datenbank |
| **Tabelle** | Strukturierte Sammlung von Daten |
| **Befehle** | SELECT, INSERT, UPDATE, DELETE |

> 💬 *„SQL-Datenbanken sind das Rückgrat moderner Anwendungen – strukturiert, zuverlässig und überall im Einsatz."*

---

## 🚀 Wie geht es weiter?

In **Lektion 2** lernst du deinen ersten SQL-Befehl in der Praxis:

```sql
SELECT * FROM Kunden;
```

➡️ *Du wirst verstehen, wie du Daten aus einer Tabelle abfragst – Schritt für Schritt!*

---

*📚 Lektion 1 von X · SQL