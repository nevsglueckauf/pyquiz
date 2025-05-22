# pyquiz
Tiny trivia game consuming Open Trivia DB (https://opentdb.com/) API 


## Prerequisites
- Python 3.13
- requests package (non-standard lib)


## Outlook / Todo
 - Generate *new* random questions fed by different (free | oss) resources 
 - (web/GUI based)
 - "static" API (using persisted data from json, php, xml files | RDBMS)

 - using "live" API of Open Trivia Database or

 - game modes:
   - web based:
     - competition
     - competion w. time limit
     - training (seeing correct answers after clicking '...spoiler')

   - CLI mode for plain text  playing in a shell 

## Appendix

### Development environment 

 Chronicler's duty: 

 - Box: Marvell MacBookAir M1 /2020 (Development)
 - Box: Thanos  iMac21,2 M1/2020 (Development)
 - Box: Raspberry Pi 4 Model B Rev 1.1 (RDBMS, CI/CD)
 - OS: Darwin Kernel Version 24.4.0; macOS Sequoia ; RELEASE_ARM64_T8103 arm64
 - OS: Linux raspberrypi 5.10.17-v7l+ #1403 SMP Mon Feb 22 11:33:35 GMT 2021 armv7l GNU/Linux
 - IDE: Visual Studio Code; version: 1.70.2 (Universal)
 - Python: Python 3.13.2
 - Java: openjdk version "11.0.18" 2023-01-17; OpenJDK Runtime Environment  & OpenJDK Server VM
 - RDBMS: Sqlite version 3.43.2
 - CI/CD pipeline: Jenkins/travis-ci



### Directory structure

<pre>

.
├── __pycache__
│   ├── app.cpython-313.pyc
│   ├── entity.cpython-313.pyc
│   ├── mock.cpython-313.pyc
│   └── trivia.cpython-313.pyc
├── app.py
├── APy.py
├── data
│   └── question.json
├── doq
│   ├── dad.md
│   └── setup.md
├── entity.py
├── grube.py
├── LICENSE
├── main.py
├── mock.py
├── README.md
├── req.txt
├── test_mock.py
├── trivia.py
└── url.php
</pre>


 
### LOC

<pre>
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           8             63             52            155
Markdown                         3             45              0            115
PHP                              1              3              0              3
JSON                             1              0              0              1
Text                             1              0              0              1
-------------------------------------------------------------------------------
SUM:                            14            111             52            275
-------------------------------------------------------------------------------

</pre>

 Nuff said for now & Glück auf! 

 Sven
