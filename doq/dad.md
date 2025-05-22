# Design & Architecture Dossier

In diesem Dokument wird die technische Umsetzung des Projektes beschrieben

## Anwendung Sequenzdiagramm Beispiel Webversion

```mermaid
sequenceDiagram
    autonumber
    UserAgent->>Webserver: https://host.example.com/trivia_game?amount={}
    Webserver->>Python: https://host.example.com/trivia_game?amount={}
    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
    UserAgent->>Webserver: Eingabe der Änderungen -> POST
    Webserver->>Python:  diff(DF, DF_edit) --> generiere SQL Stmts (UPDATE ...) 
    Python->>DB:  execute SQLs
    DB-->>Python: Ok
    Python-->Webserver: Aktualisiere Ansicht
    Webserver-->>UserAgent: Anzeige der Daten (Generiertes HTML) 
```

