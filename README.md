# PyQuiz <DEV> [^1]

>[!Disclaimer]: in German language, because of the primary audience (in my current <em>continuing education</em>) - python code: comments, function, class and variable names will be in English

## Projektidee (Abstract)

Ratespiel  mit Fragen der [Open Trivia DB](https://opentdb.com/) (und eigenen - <i>tbd.</i>) in Python in mehreren <i>[User Interfaces](https://en.wikipedia.org/wiki/User_interface)</i> ↗:

- [x] CLI (Shell / Terminal)
- [ ] GUI (tkinter???)
- [x] Web-Interface (streamlit || <del style="color:red;font-weight:bold">Django</del> <ins>!!</ins>)

[^2]

 Details zum Stand der Entwicklung finden sich [hier](doq/change_history.md).

## Weitere (projektinterne) Dokumente


- [Hinweise zum Setup](doq/setup.md) 
- [Technische Dokumentation der App](doq/dad.md) 
    - [Lastenheft lite](doq/reqspec.md)
    - [Pflichtenheft lite](doq/sysspec.md)
    - [Dokumentation des Fortschrittes der Entwicklung](doq/change_history.md)
    - [Non- "Python Standard Library" Packages](doq/non_psl_libs.md)
    - [Coding Styles](doq/ccc.md)
    - [Python spez.](doq/pydesign.md)
    - [Code Beispiele (Basic usage)](doq/code_ex.md)


## Persistenz vs. Live

Die Zusammenstellung der Fragen erfolgt aus folgenden alternativen Quellen:

1. Live Request zur API
2. Abfrage der Caches
    - 2.1 Filesystem JSON
    - 2.2 SQL DB?? (Verschoben auf ???)
    - 2.3 Sonstige (applikations-) lokale Caches??? (Verschoben auf ???)

### Motivation

Da die Aktualisierung des Fragenkatalogs seitens Trivia DB in 'überschaubarer' Frequenz erfolgt, wird dieser (applikations-) lokal gespeichert, um Latenzen
zu minimieren, resp. Netzwerkverkehr durch lokale <kbd>I/O</kbd>-Operationen zu ersetzen.




## Appendix

### Lokales Development Environment 

 - Box: Thanos  iMac21,2 M1/2020 (Development)
 - Box: Marvell MacBookAir M1 /2020 (Development)
 - Box: Raspberry Pi 4 Model B Rev 1.1 (RDBMS, CI/CD)
 - Wintendo Box: Lenovo Thinkpad (Kursinterne Kommunikation; Email)
 - OS: Darwin Kernel Version 24.4.0; macOS Sequoia ; RELEASE_ARM64_T8103 arm64
 - OS: Linux raspberrypi 5.10.17-v7l+ #1403 SMP Mon Feb 22 11:33:35 GMT 2021 armv7l GNU/Linux
 - OS: Win 11 Pro
 - IDE: Visual Studio Code; version: 1.70.2 (Universal)
 - Python: Python 3.13.2
 - Java: openjdk version "11.0.18" 2023-01-17; OpenJDK Runtime Environment  & OpenJDK Server VM
 - RDBMS: Sqlite version 3.43.2
 - CI/CD pipeline: Jenkins/travis-ci

### Foo

- Das Inline-CSS und einige HTML Attribute (z.B: ```title```) werden zwar von github beim Rendering heraus gefiltert, aber meine IDE interpretiert das wunderbar. 
Das bleibt also drin!



Glück auf!

Sven

[^1]: In frühem Entwicklungsstadium - **nicht produktionsreif!**
Der Entwicklungsforschritt wird [protokolliert](doq/change_history.md)

[^2]: Erklärung zur Task-Liste: [ ] geplant, [x] begonnen, [x] ✓ beendet