============================
Day 3 - Buildout with Tarek
============================

- Expert Python Programming book

    - TODO: Buy it at conference and get a hug
    - NOTE: Bought it and still have it as of September 2012
    
- Did Nuxeo and Zope
- got sponsored by the Plone community to come!
    
    
Part I - working with packages
===================================

distutils
----------

- Builds and distributes a package, registers and uploads it to PyPi
- screencast on http://ziade.org/ploneconf
- distutils is the standard of the whole Python community
- Alas, distutils is broken

    - but there is hope
        
setuptools
--------------

- simple dependencies management
- namespaced package
- egg distribution
- provides easy_install
- python setup.py bdist_egg

    - Eggs are to python as Jars are to Java
    - egg = deployment format in a zip archive
    - look up "sdist" which is what Tarek recommends
    
- python setup.py sdist

    - awesome sauce
    
- easy_install my_package

    - will get and install "my_package" from PyPI
        
Grrr... but setuptools is broken
--------------------------------

- setuptools is broken
- funny stuff inside
- packaging future is uncertain for python
    
Get the community behind packaging system!
------------------------------------------

- Django
- Turbogears
- etc
- Python at-large

Problems with packaging
-------------------------

1. PyPI == SPOF
2. packages need privacy sometimes
3. plone.org/products is dying

PyPI mirroring
---------------

- Make a smart mirror so it updates all the mirrors
- easy_install collective.eggproxy
- Run your own private PyPI mirror!

    - Using Plone as a host!
        

collective.dist
------------------

- python 2.6 new "register" and "upload" commands
- This lets you use these commands in older versions of Python
- Lets you push PyPI mirrors with easy config files
    
Make plone.org/products PyPI compatible
------------------------------------------

- Plone.org was suppose to switch to that for months.  Lazy guys

Big picture::

    My product  ----> plone.org
                ----> python.org
                ----> your company/agency
                
summary of part I
-------------------

    1. Make mirror
    2. Run your own PyPI
    3. Push to several servers
    4. Use "mregister" and "mupload"
    
    
----    

Part II - working with zc.buildout
===================================

local mirror::

    [buildout]
    index = http://my.mirror:8888
    
5 hours in 2006
-----------------

- took 5 hours to get a buildout running
- Developers were engineers
    
5 minutes in 2008
------------------

- get the buildout
- $ python bootstrap.py
- $ bin/buildout
- start to work
    
Not the main purpose for the creation of buildout.
--------------------------------------------------

- Reason was eggification of Zope
- Now we can updates on individual eggs rather than the whole stack
- Plone is following the same path

    - Plone pollutes Python site-packages
    - But zc.buildout isolates the plone environment

zc.buildout best practices
--------------------------

1. Use the same layout for all your projects

    - folder layout ingunieweb uses
    
        - docs
        - buildout
        - packages
        - releases
        
    - collective.releaser is what they use to handle releases
    
2. make sure all developers have the same environment

    - Windows developers are a problem
    - Get the windows installer: python2.4.4-win32.zip
    - Google "An installer for a buildout-ready Windows"
    - This should resolve the Windows issues
    
3. use on cfg per target

    - Typical buildout layout uses the **extends** feature
    
        - buildout.cfg
        - dev.cfg (extends buildout.cfg)
        - prod.cfg (extends buildout.cfg)
        - bootstrap.py


----

Part III - application lifecycle
===================================

releasing packages the old way
------------------------------------

sample::

    for package in packages:
        raise the version
        edit CHANGES.txt
        create a branch
        push to various mirrors
        make some code edits
        eggify stuff
        deploy
        etc
        
releasing package the collective.release way
-----------------------------------------------

1. Do a config file thing!
2. sample::

    for package in packages:
        release package