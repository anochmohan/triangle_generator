# triangle_generator

Write a script that prints a triangle of text. The script should take two command line inputs: the character to print, and the number of characters tall the triangle should be. 

Within your script, use functions to handle any calculations and printing. The body of your script should only contain a function call which passes the commandline input as arguments.

You must include type hints and docstrings for you functions

i.e., your script should look something like this

```python
#!/usr/bin/env python3

import sys

def func1(arg1: type, arg2: type) -> return_type:
    """Docstring"""
    ...

def func2(more_stuff: type) -> return_type:
    """Docstring"""
    ...

# The only line of code not in a function is calling a function
func1(sys.argv[1], sys.argv[2])
```

and the usage should be `<script name>.py <character> <height>`

And the output should look like this when run in a terminal

```text
$ ./q1_script.py X 5
X
XX
XXX
XX
X
$ ./q1_script.py @ 8
@
@@
@@@
@@@@
@@@@
@@@
@@
@
```