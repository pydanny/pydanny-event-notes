============================================
Giving your website a command line interface
============================================

by Michael Hudson-Doyle

About the presenter
===================

Works for Canonical and Linaro.

Enter Linaro!
--------------

The ARM ecosystem is very fragmented and the kernel has a lot of copy/paste code.

Linaro is a not-for-profit software engineering company investing in core Linux software and tools for ARM SoCs.

see: http://validation.linaro.org/

Why a command-line interface?
==============================

* We want to do things like trigger test runs when a kernal build finished
* This basically means some kind of Remote Procedure Call (RPC)

Need security
------------------

* The boards in our lab are a limited resource
* Some risk of mischief
* Eventually may have test results from unreleased hardware