# 🎓 Lektion 1: API vs. Web-Interface

**Level:** Einsteiger | **Dauer:** ~10 Minuten | **Vorkenntnisse:** keine

---

## 🎯 Lernziele

Nach dieser Lektion kannst du...

- [ ] den Unterschied zwischen API und Web-Interface erklären
- [ ] beschreiben, wofür jedes eingesetzt wird
- [ ] ein konkretes Beispiel nennen

---

## 🍽️ Stell dir ein Restaurant vor

Bevor wir technisch werden – eine Analogie, die alles erklärt:

> Du sitzt im Restaurant. Ein **Kellner** nimmt deine Bestellung auf, bringt das Essen schön angerichtet auf einem Teller. Das ist das **Web-Interface** – für dich als Mensch gemacht.
>
> Hinter der Wand gibt es eine **Küchen-Durchreiche**. Dort kommen fertige Gerichte raus – kein Tellerschmuck, keine Dekoration, direkt für die Weiterverarbeitung. Das ist die **API** – für Programme gemacht.

| | 🍽️ Web-Interface | 🔌 API |
|---|---|---|
| **Was es ist** | Speisesaal mit Kellner | Küchen-Durchreiche |
| **Für wen** | Menschen | Programme & Code |
| **Kommunikation** | Klicken, Tippen, Sehen | Strukturierte Datenpakete |
| **Ausgabe** | Bunte Webseite (HTML) | Rohdaten (meist JSON) |

---

## 👁️ Web-Interface – Für Augen und Finger

```
Du → Browser → bunte Webseite → klickst Button → siehst Ergebnis
```

**Das Web-Interface ist für Menschen gebaut.** Alles ist visuell aufbereitet, erklärt und anklickbar.

✅ Intuitiv bedienbar – kein technisches Wissen nötig
❌ Schwer automatisierbar – du musst selbst klicken
❌ Langsam bei vielen Aufgaben – stell dir vor, du musst 1.000 Städte nachschlagen

---

## 🤖 API – Für Code und Maschinen

```
Programm → sendet Anfrage → bekommt Rohdaten → verarbeitet sie weiter
```

**Die API ist für Programme gebaut.** Keine hübsche Oberfläche – nur die nackten Daten, die ein Programm braucht.

✅ Perfekt automatisierbar – läuft ohne dein Zutun
✅ Schnell & effizient – 1.000 Anfragen in Sekunden
✅ In eigene Apps integrierbar
❌ Kein visuelles Feedback
❌ Braucht Programmierkenntnisse

---

## 🌤️ Konkretes Beispiel: Wetterdaten abrufen

Beide Wege führen zum selben Ergebnis – aber auf sehr unterschiedliche Art:

**Weg 1 – Web-Interface:**
> Du öffnest `wetter.de` im Browser, siehst bunte Wolken-Icons und liest: **„Berlin – 18°C, bewölkt"**

**Weg 2 – API:**
```json
Anfrage:  GET https://api.wetter.de/berlin

Antwort:
{
  "stadt": "Berlin",
  "temperatur": 18,
  "einheit": "Celsius",
  "zustand": "bewoelkt"
}
```

> Dein Programm liest den Wert `18` und kann ihn direkt weiterverarbeiten –
> zum Beispiel: *„Wenn unter 15°C → sende Heizungs-Alarm"*

---

## 💡 Die Kernaussage

> **Web-Interface** → Ein Mensch liest das Ergebnis
> **API** → Ein Programm liest das Ergebnis

---

## 🚀 Warum APIs so mächtig sind

Du musst nicht alles selbst bauen. Stattdessen kombinierst du fertige Dienste:

```
Deine App
    ├── Google Maps API   →  Karten & Navigation
    ├── Stripe API        →  Zahlungsabwicklung
    ├── OpenAI API        →  KI-Funktionen
    └── Twitter API       →  Tweets lesen & posten
```

**Du baust auf Schultern von Riesen – ohne das Rad neu zu erfinden.**

---

## ✅ Zusammenfassung

| Frage | Antwort |
|---|---|
| Was ist ein Web-Interface? | Eine visuelle Oberfläche für Menschen |
| Was ist eine API? | Eine Schnittstelle für Programme |
| Was liefert eine API zurück? | Rohdaten, meist im JSON-Format |
| Warum sind APIs nützlich? | Automatisierung & Integration fremder Dienste |

---

## 🧪 Nächster Schritt: Selbst ausprobieren

> 💡 **Deine erste echte API:** Teste die kostenlose **OpenWeatherMap API**
> → Kostenlos, gut dokumentiert, perfekt für Einsteiger
> → [openweathermap.org/api](https://openweathermap.org/api)

**Frage zum Nachdenken:**
> *Welche App auf deinem Handy nutzt wohl im Hintergrund eine API?*
> *(Tipp: Fast jede.)*

---

*⬅️ Zurück zur Übersicht | Weiter zu Lektion 2: Wie funktioniert eine HTTP-Anfrage? ➡️*