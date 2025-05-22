# Design & Architecture Dossier

In diesem Dokument wird die technische Umsetzung des Projektes beschrieben

Der Python-spezifische Teil findet sich hier: [PyDesgin](pydesign.md)

## Persistenzschicht

- RDBMS (SQLITE, oder ???)
- Filesystem als JSON
- Filesystem als XML ???
- Filesystem als ```__pycache__``` ???


## Zur Dokumentation Allgemein

### Tools

Markdown (insbes. Mermaid) wegen der hervorragenden Unterstützung durch github

### User Interfaces

#### Shell / Terminal / Plaintext

#### GUI

#### Web

#### Sequenzdiagramm: Abruf der Fragen

```mermaid
sequenceDiagram
    autonumber
    UserAgent->>Webserver: https://host.example.com/trivia_game?amount={$FOO}
    Webserver->>Python: Generiere {$FOO} zufällige Fragen

    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
    UserAgent->>Webserver: Eingabe der Änderungen -> POST
    Webserver->>Python:  diff(DF, DF_edit) --> generiere SQL Stmts (UPDATE ...) 
    Python->>DB:  execute SQLs
    DB-->>Python: Ok
    Python-->Webserver: Aktualisiere Ansicht
    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
```

#### Sequenzdiagramm: Analyse der Antworten

```mermaid
sequenceDiagram
    autonumber
    UserAgent->>Webserver: https://host.example.com/trivia_game?amount={$FOO}
    Webserver->>Python: Generiere {$FOO} zufällige Fragen

    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
    UserAgent->>Webserver: Eingabe der Änderungen -> POST
    Webserver->>Python:  diff(DF, DF_edit) --> generiere SQL Stmts (UPDATE ...) 
    Python->>DB:  execute SQLs
    DB-->>Python: Ok
    Python-->Webserver: Aktualisiere Ansicht
    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
```

