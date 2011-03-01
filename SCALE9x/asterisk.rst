================
asterisk intro
================

SIP = almost universal VOIP protocol
IAX2 (don't use it!)
Codec used to transfer voice-to-data is ULAW

Channels = how many translations from voice-to-data you need to handle. Generally about 1 channel unless you have scaling issues.

Registration = how your box is registered to accept calls for a particular number

Asterisk can do:

 * conference calls.
 * caller ID
 * special prompts
 * voice mail
 * asterisk-to-asterisk can be free because there is no middle parties
 * telemarketer torture

AEL = Asterisk Extension language
=================================

A C-like language used to configure the behavior of an asterisk installation

Warnings!
=========

 * People can hack into your box and call Siberia.
 * SIPVicious is a tool originally written to check for hacks against Asterisk but is used to hack. 
 * Can it be placed in the cloud or do we need a datacenter?
 * The internet goes down
 * 64k bandwidth each way
 * Echos are troublesome (Open Source Echo Canceller)
 * Huge amounts of servers to run this thing
 
Changes in install screen
=========================

 * include the sounds in the codec (last three items)
 
Thoughts
========

 * check asterisk hosting
 
Resources
=========

 * O'Reilly book: Asterisk: The future of telephony