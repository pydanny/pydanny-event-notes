================================================
Blame it on Ceasar: A rant on calendaring
================================================

by Lennart Regebro

    * https://twitter.com/regebro
    * http://python3porting.com/
    * Runs a consulting shop and does really good work.

Talk Description
================

Timekeeping on all levels is surprisingly difficult. This talk explains why it's sort hard, and which parts Python can help you with.

* What is calendaring, really, and why is it so complex?
* What's in a year?
* Dissecting the Julian/Gregorian calendar
* Mesopotamian mathematics
* Time zones
* Recurring events is less fun than you think.

Introduction
==============

.. epigraph:: The problem with calendaring is that it is based off of multiple cycles that don't work well with each other

**Rome:** They had a 10 month calendar that made winter a dead period in the calendar. Eventually they added January and February

Lunar Calendars
=================

* The year is twelve lunar months long.
* The year is out of sync with the seasons
* Example: The Islamic Calendar

Lunisolar calendars
=====================

* The year is 12 or 13 months long
* The year is kept in sync with season by leap months
* examples

    * Hebrew
    * Buddhist

Solar Calendars
=================
    
.. epigraph:: The villain of the story is Caesar

* The year follows the solstices/seasons
* The moon is ignored completely
* Examples:

    * French republican
    * Julian Calendar

Thanks to the success of the Roman Empire Europe takes a weird Solar calendar, and thanks to the success of Europe, the world takes it on too.

How do you implement the calendar yourself?
===========================================

You don't. You use libraries.

* Python has datetime, date, and calendar
* JavaScript is momentjs.com, which is the current best option for JavaScript
* Java has issues thanks to an early design decision mistake.

    * http://date4j.net/
    
* The US calendar shows Sunday as the first day of the week, which is confusing because it puts the first day on the weekend.

Timezone woes
===============

* There are not 24 timezones, there are standard times per country
* standard times change
* If you want to accurate describe times from the past, you need a database of timezone changes.

Abbreviation Evil
==================

* CST

    * Australia CST
    * China Standard Time
    * Chungua Standard Time
    * US CST

Timezones are based on politics, not science.

Daylight Savings Time
=======================

* Changing the hour can cause problems with computers. Going over midnight twice breaks things.
* JavaScript handles this well
* Python handles it well

Pytz discussion
================

He gave examples of how this module does a lot of the lifting for you on timezones and daylight saving time::

    pytz 30 - 15 dateutil
    
Advantage pytz
================
    
* Works well
* Except for POSIX

Current standard specification
===============================

* TODO: Find out specified RFCs

Libraries
===========

* http://pypi.python.org/pypi/tzlocal (Download and test it out!)
* http://pypi.python.org/pypi/icalendar
* http://pypi.python.org/pypi/DateUtils

Datepickers
=================

* Based on JavaScript if you are doing the web
* http://arshaw.com/fullcalendar/
* https://github.com/collective/jquery.recurrenceinput.js