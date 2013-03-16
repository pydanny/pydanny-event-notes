================================
Porting Django apps to Python 3
================================

Django 1.5 now supports Python 3, so now's the time to start thinking about porting your apps and sites. Come see how! I'll talk about the porting techniques that work, and present two case studies: porting a site, and porting a reusable app.

by Jacob Kaplan-Moss

    * Django co-creator and BDFL
    * https://github.com/jacobian / https://twitter.com/jacobian


Do I want to use Python 3?
=============================

* Yes!
* Python 3 has fewer warts

    * urllib / urllib2 replaced with urlparse
    * std library cleanup
    