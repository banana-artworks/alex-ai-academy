# 🌐 Lektion 1: HTML, CSS & JavaScript – Das Traumteam des Webs

---

## 🎯 Was lernst du in dieser Lektion?

Am Ende dieser Lektion weißt du:
- ✅ Was HTML, CSS und JavaScript **sind**
- ✅ Welche **Aufgabe** jede Technologie hat
- ✅ Wie die drei **zusammenarbeiten**
- ✅ In welcher **Reihenfolge** du sie lernen solltest

---

## 🏗️ Stell dir ein Haus vor

Bevor wir ins Technische gehen – hier eine Analogie, die alles erklärt:

> 🏠 **Eine Webseite ist wie ein Haus.**

| Technologie | Rolle im Haus | Was sie macht |
|-------------|---------------|---------------|
| **HTML** | 🧱 Das Gerüst | Gibt Struktur und Inhalt |
| **CSS** | 🎨 Die Dekoration | Bestimmt das Aussehen |
| **JavaScript** | ⚡ Die Elektronik | Macht alles interaktiv |

> 💬 **Merke:** Ein Haus ohne Gerüst fällt um. Dekoration ohne Gerüst hat nichts, woran sie hängt. Und Lichtschalter ohne beides sind nutzlos.
> **Genauso brauchen alle drei einander.**

---

## 🧱 HTML – Die Struktur

### Was ist HTML?

**HTML** steht für **H**yper**T**ext **M**arkup **L**anguage.
Es ist die **Grundlage jeder Webseite** – ohne HTML gibt es nichts zu sehen.

### Was macht HTML?

HTML beantwortet die Frage:
> **„Was steht auf der Seite?"**

Es legt fest:
- Überschriften
- Texte
- Bilder
- Buttons
- Links

### Wie sieht HTML aus?

HTML arbeitet mit sogenannten **Tags** – das sind Bausteine in spitzen Klammern:

```html
<h1>Willkommen!</h1>
<p>Das ist mein erster Text.</p>
<button>Klick mich!</button>
```

### Was passiert damit?

➡️ Du siehst eine Überschrift, einen Absatz und einen Button.
⚠️ Aber: Alles ist noch **unformatiert und funktionslos**.

---

## 🎨 CSS – Das Aussehen

### Was ist CSS?

**CSS** steht für **C**ascading **S**tyle **S**heets.
Es ist die **Gestaltungssprache** des Webs.

### Was macht CSS?

CSS beantwortet die Frage:
> **„Wie sieht es aus?"**

Es steuert:
- Farben & Schriften
- Abstände & Größen
- Layouts & Positionen
- Animationen & Effekte

### Wie sieht CSS aus?

```css
h1 {
  color: blue;
  font-size: 32px;
}

button {
  background-color: green;
  border-radius: 8px;
}
```

### Was passiert damit?

➡️ Die Überschrift wird **blau**, der Button bekommt **grüne Farbe und runde Ecken**.
⚠️ Aber: Der Button **tut noch nichts**, wenn man ihn klickt.

---

## ⚡ JavaScript – Die Interaktivität

### Was ist JavaScript?

**JavaScript** ist eine **Programmiersprache**, die direkt im Browser läuft.
Sie ist das **Gehirn** der Webseite.

### Was macht JavaScript?

JavaScript beantwortet die Frage:
> **„Was passiert, wenn ich etwas tue?"**

Es reagiert auf:
- Klicks
- Tastatureingaben
- Mausbewegungen
- Formular-Absendungen

Und kann dabei:
- Inhalte **verändern**
- Daten **verarbeiten**
- Mit Servern **kommunizieren**

### Wie sieht JavaScript aus?

```javascript
button.addEventListener("click", function() {
  alert("Du hast geklickt! 🎉");
});
```

### Was passiert damit?

➡️ Der Button **reagiert auf Klicks** und zeigt eine Nachricht an.
✅ Jetzt ist die Seite wirklich lebendig!

---

## 🔄 So arbeiten alle drei zusammen

Wenn du eine Webseite öffnest, passiert folgendes – in dieser Reihenfolge:

```
1. 🧱 HTML lädt
   → Die Struktur der Seite steht
         ↓
2. 🎨 CSS wird angewendet
   → Die Seite sieht gut aus
         ↓
3. ⚡ JavaScript startet
   → Die Seite wird interaktiv
```

> 💬 **Wichtig:** Alle drei laufen im **Browser** des Nutzers –
> du musst nichts installieren, um loszulegen!

---

## 💡 Die drei goldenen Fragen

Immer wenn du verwirrt bist, frag dich:

| Frage | Zuständig |
|-------|-----------|
| **Was** ist auf der Seite? | 🧱 HTML |
| **Wie** sieht es aus? | 🎨 CSS |
| **Was passiert**, wenn ich etwas tue? | ⚡ JavaScript |

---

## 🗺️ Dein Lernpfad

```
Schritt 1 → HTML lernen    (Struktur verstehen)
Schritt 2