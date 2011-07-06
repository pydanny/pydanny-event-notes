Untested code is broken code
======================================

.. note:: Some of this stuff is awesome and I use it every day. The doctest stuff led me astray and I'm glad to be free. (Danny 07/05/2011)

by Martin Aspeli and Philp von Weiterhausen

arguments against
===================

    - they take time to write
    - I'm a good developer
    - my customer/community does the testing

justification
===================

    - You rarely catch subtle problems
    - put the time you spend writing silly bugs into writing tests
    - you end up saving time when you refactor

tests in python
===================

    - Easy, especially in Python

Test driven development
======================================

    - Write the test first
    
      - You don't forget to write the tests
      - You can catch design mistakes early on

Executable documentation
========================

.. note:: This section was designed to support *doctests*. Now I advocate unittests, sphinx, and rtfd.org (Danny 07/05/2011)

    - Tests should excercise APIs, demonstrate how to use them
    - Developers may find documentation in tests
    - Why not turn them into documentation?

doctests
===================

.. warning:: Use doctests and you'll hate yourself later, I'm keeping this for the sake of history (Danny 07/05/2011)

    - looks like an interpreter session
    - restructured text
      - can be rendered to HTML, PDF, etc

documentation-driven development
=================================

    - write unittests first
    - science fixture
    - tell a story to an imaginary user
    - use 'we' and 'you'
    - put the story on the product home page!!!
    - Danny likes this idea tons!

General Test concepts
=====================

    - Each test should be totally independent of other tests
    - Only load the bits you need, don't load all components!  So...

      - Use zope.component.provideAdapter(UpperCaser)
      - zope.testing.doctest.DocFileSuite(..,...,..,teardown=True)
      - $instance test
  
    - Don't use: from Testing import ZopeTestCase unless you are doing integration

    - from Products.Five.testbrowser import Browser

      - Simulates browser actions
      - learned in the class
