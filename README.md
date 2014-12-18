NS Code Sample
==============

Setup
-----

This code sample is written to use Python 3, and has a
virtualenv-based deployment system. These dependencies must be
installed using these commands (or equivalent):

    $ apt-get install python3 python-virtualenv

Then, to set up the environment just run the included setup script.

    $ ./setup-develop.sh

Running
-------

After environment setup, the main script to run the program is found
in `bin/ns_demo`. A sample input file (as per the spec) is included as
`sample.txt`.

    $ bin/ns_demo sample.txt
    CATEGORY    COUNT
    PERSON    2
    PLACE    2
    ANIMAL    2
    COMPUTER    1
    OTHER    1
    PERSON    Bob Jones
    PLACE    Washington
    PERSON    Mary
    COMPUTER    Mac
    OTHER    Tree
    ANIMAL    Dog
    PLACE    Texas
    ANIMAL    Cat

The code is found under `src/ns_sample`.

Testing
-------

Testing is done using the `nose` testing suite, and can be run by
simply using:

    $ bin/nosetests
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.004s
    
    OK

