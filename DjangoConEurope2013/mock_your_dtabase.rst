====================
Mock your database
====================

by Marc Tamlyn

Databases are slow. Well, if the goal is 1 millisecond per test they are anyway. We want to avoid interacting with the database as much as possible when testing, especially if the tests aren't anything to do with the queries.

This talk will look at various ways of avoiding those pesky database queries and making tests faster!