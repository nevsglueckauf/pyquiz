# PyQuiz <DEV> [^1]

>[!Disclaimer]: in German language, because of the primary audience (my current <em>continuing education</em>)


Ratespiel  mit Fragen der [Open Trivia DB](https://opentdb.com/) (und eigenen - <i>tbd.</i>) in Python in mehreren <i>[User Interfaces](https://en.wikipedia.org/wiki/User_interface)</i> - (externer Link):

- [x] CLI (Shell/Termin)
- [ ] GUI (tkinter???)
- [ ] Web-Interface (streamlit || Django ??)


Obige Task liste spiegelt den Stand der Entwicklung wieder ([x] meint angefangen/beendet)

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

- [Hinweise zum Setup](doq/setup.md) 
- [Technische Dokumentation](doq/dad.md) 



- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...
- [x] ...
- [ ] ...

- [ ] ...
- [ ] ...
- [ ] ...
- [ ] ...
- [x] ...
- [ ] ...







[^1]: In Entwicklung - **nicht produktionsreif!**
Der Enticklungsforschritt wird [protokolliert](doq/change_history.md)