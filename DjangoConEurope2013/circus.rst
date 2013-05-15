====================================
Circus: process & socket manager
====================================

* By Tarek Ziade

Circus is a process manager we developped at Mozilla while working on high scalability, we wanted to have a way to deal with our processes directly from python, and in a better way that's what possible with the standard library.

Circus uses zeromq in its internals, and thus is easily extensible. We'll present you how you why we built circus, how to use it and some core concepts that were useful in the conception of the tool. Also, we'll demonstrate how easy it is to plug circus with a Django stack.

Typical Django Deployment
==============================

* Nginx > Gunicon > Django + sentry + celery


Supervisord is frequently used for management of these components. Alternatives include:

*  Bluepill (less mature)
* upstart (system level - root access needed)
* daemontools (low-level like upstart)
* got, monit, runit, etc.

Missing features from supervisord
==================================

* Realtime stdout/stderr
* realtme stats
* powerful web console
* Remote access
* clustering
* event-based plugins

Since those were missing, Tarek launched his own project: Circus!