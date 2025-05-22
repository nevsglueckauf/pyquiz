# PyQuiz <DEV> [^1]

>[!Disclaimer]: in German language, because of the primary audience (my current <em>continuing education</em>)

## Projektidee (Abtract)
Ratespiel  mit Fragen der [Open Trivia DB](https://opentdb.com/) (und eigenen - <i>tbd.</i>) in Python in mehreren <i>[User Interfaces](https://en.wikipedia.org/wiki/User_interface)</i> - (externer Link):

- [x] CLI (Shell/Termin)
- [ ] GUI (tkinter???)
- [ ] Web-Interface (streamlit || Django ??)

Obige Task Task-Liste spiegelt den Stand der Entwicklung wieder ([x] meint angefangen/beendet) Details sind [hier](doq/change_history.md).

## Weitere (projektinterne) Dokumente

- [Hinweise zum Setup](doq/setup.md) 
- [Technische Dokumentation](doq/dad.md) 
    - [Lastenheft lite](doq/reqspec.md)
    - [Pflichtenheft lite](doq/sysspec.md)
    - [Dokumentation des Fortschrittes der Entwicklung](doq/change_history.md)




## Persistenz vs. Live

Die Zusammenstellung der Fragen erfolgt aus folgenden alternativen Quellen:

1. Live Request zur API
2. Abfrage des Caches
    - 2.1 Filesystem JSON
    - 2.2 SQL DB??
    - 2.3 Sonstige (applikations-) lokale Caches???

### Motivation

Da die Aktualisierung des Fragenkatalogs seitens Trivia DB in 'überschaubarer' Frequenz erfolgt, wird dieser (applikations-) lokal gespeichert, um Latenzen
zu minimieren, resp. Netzwerkverkehr durch lokale <kbd>I/O</kbd>-Operationen zu ersetzen.

[^1]: In frühem Entwicklungsstadium - **nicht produktionsreif!**
Der Enticklungsforschritt wird [protokolliert](doq/change_history.md)