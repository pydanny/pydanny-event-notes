=================================================
Healthy Webapps Through Continuous Introspection
=================================================

by Erik van Zijst

* http://twitter.com/erikvanzijst
* http://butbucket.org/evzijst

Wasted cycles on Bitbucket
============================

=> SSHD => conq (Python) => git/hg

* conq is our custom SSH shell
* conq imports Django ORM and Bitbucket code
* takes ~1.41 seconds to start (spawns ~50/second)