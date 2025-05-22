# Design & Architecture Dossier

## Sequence diagram 

```mermaid
sequenceDiagram
    autonumber
    
    App->>API: https://opentdb.com/api.php?amount={:AMOUNT}
    API-->>App: List of questions (JSON)
    App->>Python:  Parse JSON, generate entity instances 
    Python->>App:  "mix corr./ incorr. answers, shuffle answer order, render question view"
    App-->>User: Show rendered trivia game
    User-->>App: Input (for answers) + <SUBMIT>

```

