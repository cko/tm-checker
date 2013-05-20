tm-checker
==========

Script to check if common IT event formats are registered as trademark in the DPMA database (like 'Hackathon': https://register.dpma.de/DPMAregister/marke/register/3020120063403/DE).

Prerequisites
-------------
- Python 2.7
- virtualenv

Usage
-----

    $ cd tm-checker
    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate
    $ pip install mechanize
    $ python tm-checker.py

The words to be checked are configured via words.txt
