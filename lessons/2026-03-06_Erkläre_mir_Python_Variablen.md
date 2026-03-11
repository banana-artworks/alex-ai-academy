# 🐍 Python-Lektion: Variablen

## 🎯 Lernziele

Nach dieser Lektion kannst du…
- ✅ erklären, **was** eine Variable ist und **wozu** sie dient
- ✅ Variablen korrekt **erstellen und benennen**
- ✅ **Datentypen** unterscheiden und prüfen
- ✅ **Scope** und **Mehrfachzuweisung** sicher anwenden

---

## 1 · 📦 Was ist eine Variable?

Stell dir eine Variable wie eine **beschriftete Box** vor:

```
┌─────────────────┐
│   name = "Max"  │
│   📦 "Max"      │
└─────────────────┘
```

> Eine Variable ist ein **benannter Verweis** auf ein Objekt im Arbeitsspeicher.
> Sie speichert einen Wert, den du später lesen oder verändern kannst.

**In Python gilt:**
- 🚫 Keine Deklaration nötig (`int x;` wie in C gibt es nicht)
- 🏷️ Kein Typ muss angegeben werden
- ➡️ Zuweisung erfolgt mit `=`

```python
name  = "Max"   # 🔤 String
alter = 25      # 🔢 Integer
preis = 9.99    # 💲 Float
aktiv = True    # ✅ Boolean
```

---

## 2 · 📝 Namensregeln

Bevor du eine Variable erstellst, musst du wissen, **wie sie heißen darf**.

### ✅ Erlaubt
| Regel | Beispiel |
|-------|----------|
| Buchstaben (a–z, A–Z) | `name` |
| Zahlen (nicht am Anfang) | `name1` |
| Unterstriche | `_name`, `mein_name` |

### ❌ Nicht erlaubt
| Verstoß | Falsches Beispiel |
|---------|-------------------|
| Beginnt mit Zahl | `1name` |
| Sonderzeichen | `name!`, `mein-name` |
| Leerzeichen | `mein name` |
| Python-Schlüsselwort | `if`, `for`, `class` |

### 🧪 Selbsttest – Was ist gültig?

```python
_wert     = 10      # ✅ oder ❌ ?
2temp     = 5       # ✅ oder ❌ ?
mein_wert = 99      # ✅ oder ❌ ?
class     = "A"     # ✅ oder ❌ ?
```

<details>
<summary>💡 Lösung anzeigen</summary>

```
_wert     ✅  – Unterstrich am Anfang ist erlaubt
2temp     ❌  – Beginnt mit einer Zahl
mein_wert ✅  – Unterstrich statt Leerzeichen
class     ❌  – Python-Schlüsselwort
```
</details>

---

## 3 · 🔄 Dynamische Typisierung

Python erkennt den Typ **automatisch** – und er kann sich jederzeit ändern:

```python
x = 10        # 🔢 x ist Integer
x = "Hallo"   # 🔤 x ist jetzt String – kein Fehler!
x = 3.14      # 💫 x ist jetzt Float
```

> 💡 Das nennt sich **dynamische Typisierung**.
> Der Typ steckt im **Objekt**, nicht in der Variable.

---

## 4 · 🗂️ Datentypen im Überblick

| Typ | Beispiel | Bedeutung |
|-----|----------|-----------|
| `int` | `42` | 🔢 Ganzzahl |
| `float` | `3.14` | 💫 Dezimalzahl |
| `str` | `"Hallo"` | 🔤 Zeichenkette |
| `bool` | `True / False` | ✅ Wahrheitswert |
| `list` | `[1, 2, 3]` | 📋 Veränderliche Liste |
| `tuple` | `(1, 2, 3)` | 🔒 Unveränderliches Tupel |
| `dict` | `{"key": "val"}` | 🗝️ Schlüssel-Wert-Paare |
| `None` | `None` | 🚫 Kein Wert |

### 🔍 Typ prüfen & umwandeln

```python
x = 42
type(x)              # → <class 'int'>
isinstance(x, int)   # → True

# 🔁 Konvertierung
str(42)              # → "42"
int("10")            # → 10
float(5)             # → 5.0
```

---

## 5 · ⚡ Mehrfachzuweisung

Python erlaubt elegante Kurzschreibweisen:

```python
# 🎯 Mehrere Variablen auf einmal
a, b, c = 1, 2, 3

# 🔗 Gleicher Wert für alle
x = y = z = 0

# 🔀 Werte tauschen – ohne Hilfsvariable!
a, b = b, a
```

> 💡 Der Tausch `a, b = b, a` ist **Python-spezifisch** und besonders praktisch.

---

## 6 · 🌍 Gültigkeitsbereiche (Scope)

Wo eine Variable **gültig** ist, hängt davon ab, wo sie erstellt wurde.

```
📐 LEGB-Regel:
Local → Enclosing → Global → Built-in
```

```python
x = "global"  # 🌍 Globale Variable

def funktion():
    x = "lokal"   # 📦 Eigene, neue Variable
    print(x)      # → "lokal"

print(x)          # → "global"
```

| Scope | Gültig… |
|-------|---------|
| 🔹 **Local** | Nur innerhalb der Funktion |
| 🔸 **Enclosing** | In äußerer Funktion (bei Verschachtelung) |
| 🌍 **Global** | Im gesamten Modul |
| 🏗️ **Built-in** | Überall (z. B. `print`, `len`) |

---

## 7 · 🔒 Konstanten & Besonderheiten

### 📌 Konstanten (Konvention)
```python
MAX_WERT = 100    # 🔠 GROSSBUCHSTABEN signalisieren: „bitte nicht ändern"
PI       = 3.14159
```
> ⚠️ Python erzwingt das **nicht** – es ist reine Vereinbarung.

### 🛠️ Weitere nützliche Fakten

```python
id(x)               # 🧭 Speicheradresse des Objekts
del x               # 🗑️ Variable löschen
name: str = "Max"   # 🏷️ Type Hint (ab Python 3.5)
```

---

## 8 · 📊 Zusammenfassung

```
🧩 Variable = Name + Wert + Typ + Speicheradresse
```

| Eigenschaft | Python |
|-------------|--------|
| 🔄 