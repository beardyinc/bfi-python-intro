# bfi-python-intro
Feel free to use this repository as template for practical python examples.
The try to cover a few basic topics:
1. loops
2. if-statements
3. functions
3. unit tests (to verify the code) 

# how to run the tests
simply call `python unittests.py` from a command line of your choice

# how to run commandline programs
many of the python scripts have a `run()` method that runs the commandline program. On the shell of your choice execute the following steps:
```
python

>>> import binary

>>> binary.run()

```
This will call the (very simple) CLI. 

# ```binary.py```
Contains a function `to_binary`that converts an integer into its binary representation (`str`). 

# `factorial.py`
Contains a function `calc_factorial` that computes the factorial for any given positive integer `N`.

# `primecheck.py`
Contains a function checking if a given number is a prime.

# `primeseq2.py`
Computes all prime numbers up to a given upper limit.

# `car_management.py`
contains a small program reading input from `stdin` along some basic error handling.


## Please note 
that this repository serves the sole purpose of demonstrating *very basic semantic concepts* to an audience with little to no programming knowledge. 
I know very well that in production software one would do things differently, but for the sake of clarity much of the usual project setup has been ditched. 