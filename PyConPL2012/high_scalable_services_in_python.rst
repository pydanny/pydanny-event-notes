==================================
Highly scalable services in Python
==================================

Original title: `Wysoko skalowalne serwisy pythonowe w OnetPoczcie`

* by Igor Waligóra

    * From Warsaw
    * Works on high integrity systems

.. note:: I'm translating this entire talk from Polish.
    I don't speak Polish except how to say, "Thanks" and now "Questions?".


Talk Description (In Polish)
============================

W prezentacji pokażemy nasz model rozproszenia usług pocztowych, jak zrobiliśmy to przy użyciu Pythona. Pokażemy metody realizacji stabilnych i skalowalnych systemów utylizujących niskopoziomowe biblioteki oraz model ich zwielokrotnienia i integracji. Uchylimy rąbek tajemnicy działania jednego z największych systemów pocztowych w polskim Internecie.

System Architecture
====================

Some sort of email system

* 200 servers
* 20 database servers
* 1 Petabyte of data
* 4.7 million users
* 80 thousand requests a minute
* Spam

Server types
--------------

* SMTP

    * Postfix > MDA > Storage

* POP3 / IMAP

    * Dovecot > storage
    
* Webmail

    * PHP / JavaScript > Python Server > Storage