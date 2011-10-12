=======================
Re-Introduction to C
=======================

* By Noah Kantrowitz
* Good speaker, knows topic
* Should have gone over fundamentals in second half before having us code
* My proposed change

    # Insist people type out working code example presented (muscle memory)
    # Brain dump (what was second half)
    # Another insist type out of working code example based on brain dump material
    # Go to attendee excercises where they have to figure things out themselves

Talk Notes
-----------

Stack vs Heap
==================

* Stack is very specific memory buffers
* Heap is everything else

Pointer Arithmetic
==================

C knows how many bytes in each variable:

.. sourcecode:: c

    int arr[10];
    arr = 1000
    arr + 1 = 1004
    char arr2[10];
    arr2 = 1000
    arr2+1 == 1001

Strings
========

.. sourcecode:: c

    char*s = "abc";
    *s == 'a';
    char s[4] = "abc";
    *(s+1)=='b';

Structures
===========

Structures are the closest in C to having OO style classes. Use **typedef** to ensure that you can more easily construct the structure.

* Named+typed offsets
* **Syntax**:

.. sourcecode:: c

    `typedef struct Foo {int x; char y;} Foo;`

* Inside the curly braces you can stick in variables to be called on instantiation

.. sourcecode:: c

    Foo f = {1,2};
    f.x==1;
    Foo f = {0};

    * Useful in that everything is set to Zero even if there is more than one variable. Even works with chars! Yay
    
Unions
=======

Rare thing used in C, and then specifically for high performance C.

* Also named+typed offsets
* Overlapping (?)
* **syntax**: 

.. sourcecode:: c

    typed union Foo {int x; char y[4];} Foo;
    f.y[3] = 1;
    f.x == 0x01000000;

Enumerations
=============

Enumerations are symbolic references to numbers. While numbers you should not do math on them. Nice syntax sugar.

* **syntax**:

.. sourcecode:: c

    typedef enum Foo {BAR, BAZ} Foo;

* BAR is equal to 0
* BAZ is equal to 1

.. sourcecode:: c

    Foo f = BAR;
    f = 1;
    BAR + 1;
    BAZ == BAR + 1;

Comments
========

Same as in JavaScript.

Function Declarations
=====================

* `int foo(int x, char y);`

    * returns int
    * accepts int x and char y.

* `void foo(void);`

    * Don't return anything
    * Don't accept any arguments
    
* `void foo();`

    * Don't return anything
    * Accept any number of arguments

If C cannot find something it will report an Int error

Main
====

This is why python has `"__name__" == "__main__"`!

.. sourcecode:: c

    int main(int argc, char **argv);
    ./prog foo bar
    argc == 3
    argv == {"./prog", "foo", "bar"}

printf
======

How to do a print in C:

.. sourcecode:: c

    #include <stdio.h>
    def printf(fmt, *args) return fmt%args
    printf("%s %u\n", "foo", 42);

* Coming from a user do this to make sure that their percent signs (%) are not accidentally made part of the format strings:

    * `printf("%s", s);`
    
blocks
======

Blocks are curly braces and then statements. **Variable statements must happen at the top of a block**.

.. sourcecode:: c

    { stmt; stmt; }
    if (expr) stmt; else stmt;
    if (){} else {};
    if () {int x=0; foo(x);}
    if (x==1){y=1;} else if (x==2) {y=2;};

while
=====

Same as python

.. sourcecode:: c

    while (x==0){y++;}

do while
=========

Same as while but runs it once first

Switch
=======

Basically a structured GOTO system that jumps to each case as in other languages. How I think it works if expr evaluates to a number (confirm later):

.. sourcecode:: c

    switch (expr)
        {
            case 1: {
                    y = 1;
                    break;
                };
            case 2:
                y = 2;
                break;
            default:
                y = 3;
        }
        
Preprocessor
============

Transforms your code before it hits the compiler. Don't use '#' to start any lines except for directives!

* #include

    * Takes the entire contents of this file and pastes it in. Not quite import!
    * `#include "file.h"` looks in the local path
    * `#include <stdio.h>` looks in the system libraries

* #define

    * Values that the preprocessor replaces (simple macros)
    * `#define Y 1.0` now works in the rest of the file. Think of it as a global. Can't do C expressions but can define text based replacements.
    * Don't put semi-colons at the end of a #define macro.
    
* #define can take arguments!

.. sourcecode:: c

    #define Z(a,b) foo (A * 2, b, 0)
    Z(1,2);
    foo(x +1 * 2, 2, 0);
    `#define Z(a,b) foo((a) * 2, (b), 0)

* #if include other preprocessor bits:

.. sourcecode:: c

    #if X
        #define Y 1.0
        #include "file.h"
    #endif
    
* `#ifdef` is used in older code and is simply `#ifdefined(X)`.

* `#pragma once`

    * Include guard
    * Makes sure you include something only once since you might have multiple files including the same thing and that can be bad.
    * Don't do `#ifdef __FILE_H__`!
    
Headers
=======

Headers are files that end in '.h' and contain function declarations. This way the compiler knows what functions are going to be used:

.. sourcecode:: c

    #pragma once

    void handle_request(int sockfd, const char *request);

Sometimes you see `typedef struct Foo Foo` and this is to just let the compiler know there will be a struct called Foo.

Useful functions
================

* string.h

    * length: `size_t strlen(const char *s)`
    * compare: `strcmp(char *s1, char *s2)`
    * copy: `*strncpy(char *s1, char *s2, size_t n);`
    * `memcpy(void *s1, void *s2, size_t n)`

* malloc (buffer management)

    * `#include <stdlib.h>`
    * `void *malloc(size_t)`
    * `void free(void *ptr)`
    * `void *calloc(size_t count, size_t size)`
    
* stdio.h (I/O handling - files writing and reading)

Runtimes
=========

Check out: http://docs.python.org/c-api/

Convore
==================

https://convore.com/pycon-2011/reintro-to-c-tutorial/