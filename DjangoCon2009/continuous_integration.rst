======================
Continuous Integration
======================

 * A way to make deployments and releases stronger
 
Assumptions and Constraints
===========================

 * CI includes running tests
 * VCS must be part of things
 * Compiling

What is CI?
===========

 * As a developer saves to the VCS it pulls the code, runs the tests, and reports.
 * Can be done nightly, daily, or per VCS commit.
 * Build artifacts need to be handled. A build artifact is data and other non-code pieces.
 
Tests
======
    
    * Integration
    * Functional
    * Code inspection