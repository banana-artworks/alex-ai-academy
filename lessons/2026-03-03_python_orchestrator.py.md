# 🐍 Python Lektion 1: Der Orchestrator

## Lernziele

Nach dieser Lektion kannst du:
- ✅ Erklären, **was** ein Orchestrator ist
- ✅ Den **Aufbau** einer `orchestrator.py` lesen und verstehen
- ✅ Mindestens **einen Anwendungsfall** nennen

---

## 1️⃣ Was ist ein Orchestrator?

Ein **Orchestrator** ist wie ein **Dirigent** – er gibt nicht selbst Geige oder Trompete, aber er sorgt dafür, dass alle **im richtigen Moment** einsetzen.

> 💡 **Merksatz:** Der Orchestrator macht nichts selbst – er sagt anderen, **was sie wann tun sollen.**

---

## 2️⃣ Die Pizza-Analogie

Stell dir vor, du bestellst eine Pizza:

```
🍕 Bestellung eingeht
        ↓
👨‍🍳 Koch backt die Pizza       ← Schritt 1
        ↓
📦 Lieferant holt sie ab       ← Schritt 2
        ↓
💳 Kasse bucht die Zahlung     ← Schritt 3
```

**`orchestrator.py` = der Restaurantmanager**

Ohne ihn würde der Lieferant losfahren, **bevor die Pizza fertig ist.** 🚴‍♂️💨

---

## 3️⃣ Was macht `orchestrator.py` konkret?

| Aufgabe | Was passiert dabei? |
|---|---|
| 🔀 **Koordination** | Steuert andere Skripte oder Dienste |
| 🔢 **Reihenfolge** | Legt fest, was **wann** ausgeführt wird |
| ⚠️ **Fehlerbehandlung** | Reagiert, wenn etwas schiefläuft |
| 👁️ **Monitoring** | Überwacht den Status aller Aufgaben |

---

## 4️⃣ Dein erstes Code-Beispiel

Lies den Code Zeile für Zeile. Du musst ihn noch nicht selbst schreiben!

```python
# orchestrator.py – dein erstes Beispiel

# ── Die einzelnen Aufgaben ──────────────────────────
def schritt_1():
    print("📥 Daten laden...")

def schritt_2():
    print("⚙️  Daten verarbeiten...")

def schritt_3():
    print("💾 Ergebnis speichern...")


# ── Der Orchestrator ────────────────────────────────
def main():
    schritt_1()   # ① Erst laden
    schritt_2()   # ② Dann verarbeiten
    schritt_3()   # ③ Dann speichern


# ── Startpunkt des Programms ────────────────────────
if __name__ == "__main__":
    main()
```

### 🔍 Was passiert hier?

```
main() wird aufgerufen
    │
    ├─► schritt_1()  →  "Daten laden..."
    ├─► schritt_2()  →  "Daten verarbeiten..."
    └─► schritt_3()  →  "Ergebnis speichern..."
```

> ⚠️ **Wichtig:** Die Reihenfolge ist **kein Zufall** – sie ist das Herzstück des Orchestrators!

---

## 5️⃣ Wo begegnet dir das in der Praxis?

```
🤖 KI-Systeme       →  Mehrere KI-Agenten koordinieren
📊 Datenpipelines   →  Daten laden → prüfen → speichern
☁️  Cloud-Dienste   →  Microservices steuern
🔄 Automatisierung  →  Wiederkehrende Aufgaben automatisieren
```

---

## 6️⃣ Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| **Orchestrator** | Steuert und koordiniert andere Programme |
| **`main()`** | Der Startpunkt – ruft alle Schritte auf |
| **Reihenfolge** | Entscheidend für korrekte Ergebnisse |
| **`if __name__ == "__main__"`** | Stellt sicher, dass `main()` nur direkt gestartet wird |

---

## 🧠 Verständnisfragen

Beantworte diese Fragen für dich – ohne nachzuschauen:

1. Was ist der Unterschied zwischen dem **Orchestrator** und den **einzelnen Schritten**?
2. Was würde passieren, wenn man `schritt_3()` **vor** `schritt_1()` aufruft?
3. Nenne ein eigenes Beispiel aus dem Alltag, das wie ein Orchestrator funktioniert.

---

## 🚀 Nächste Schritte

Wenn du bereit bist, bauen wir in **Lektion 2** einen Orchestrator mit:
- ✳️ Fehlerbehandlung (`try / except`)
- 🔁 Schleifen für wiederholte Aufgaben
- 📋 Logging – damit du siehst, was gerade passiert

---

*Lektion 1 von N · Schwierigkeitsgrad: Einsteiger 🟢*