===============
Database Design
===============

Pure SQL Implementation
=======================

All tables are assumed to have an ID.

Pros:

 * All data in one database means simpler architecture
 * All staff familiar with SQL
 * SQL is proven
 
Cons:

 * Django Admin becomes unwieldy with complex inlines.
 * Requires sophisticated Python logic to handle Survey display and controls.
 * Saving survey state is rigid and will make changing the survey model much harder. 
 * Survey and survey state make saving and fetching historical surveys very rigid. Post-launch might need to make new tables after any change to ensure no historical data is lost.
 * Adding sub-surveys adds in a huge amount of complexity

client
------

Represents customer for a particular survey

 * name
 * point_of_contact

user
----

 * name
 * email
 * password

profile
-------

 * address_1
 * address_2
 * city
 * state
 * zip
 * dob
 * gender
 * occupation
 * employer   
 * address_verified
 * dob_verified
 * employment_verified
 
survey
-------

 * title
 * description
 * start_date
 * end_date 
 * max_responses
 * value_per_response
 * verification_level
 * client_id

media
------

 * id
 * url
 * **Optional**: survey_id
 
media_survey
------------

**Question**: Can a survey have multiple media elements that are shared across
other surveys? If not, then we probably can remove this table.

 * survey_id
 * media_id

question
---------

 * label
 * order (within the survey)
 * type (radio, select, checkbox, text, textarea)
 * survey_id

response
--------

 * value (integer, boolean, or text)
 * question_id
 * user_id

survey_state
-------------

Saves the state of a survey for a user.

 * completed
 * start_date
 * end_date
 * user_paid 
 * survey_id
 * user_id
 
----

SQL + Mongo Implementation
===========================

All tables are assumed to have an ID.

Pros:

 * User/Financial data separate from survey data. Faster results for both.
 * Financial data in SQL, which was designed for that task.
 * Doesn't replace critical components of Django (Session, Auth, User with unproven MongoDB components)
 * Survey logic changes much easier to implement in Mongo, just new app for each alteration.
 * Survey and Response documents store historical survey app so continue to work over time.
 * Adding sub-surveys is of moderate complexity
 * Simpler display and controls of Surveys
 * BSON/JavaScript interface
 
Cons:

 * Need to construct survey forms from scratch (will have to do that in any implementation)
 * New technology to most of the staff
 * MongoDB adds complexity to the architecture
 * Local deployments harder

client (SQL)
------------

Represents customer for a particular survey

 * name
 * point_of_contact

user (SQL)
----------

 * name
 * email
 * password

profile (SQL)
-------------

 * address_1
 * address_2
 * city
 * state
 * zip
 * dob
 * gender
 * occupation
 * employer   
 * address_verified
 * dob_verified
 * employment_verified
 
survey (SQL)
------------

 * title
 * description
 * start_date
 * end_date 
 * max_responses
 * value_per_response
 * verification_level
 * client_id

media (SQL)
-----------

 * id
 * url
 * **Optional**: survey_id
 
media_survey (SQL)
------------------

**Question**: Can a survey have multiple media elements that are shared across
other surveys? If not, then we probably can remove this table.

 * survey_id
 * media_id

survey_state (SQL)
-------------------

Saves the state of a survey for a user.

 * completed
 * start_date
 * end_date
 * user_paid 
 * survey_id
 * user_id
 
survey_document (MongoDB)
-------------------------

 * survey_id (used to relate to SQL)
 * survey_app (we create new Django app for new versions of surveys)
 * questions (list/array)

    * label
    * type (radio, select, checkbox, text, textarea) 
 
response_document (MongoDB)
----------------------------

 * survey_document (copy of the survey_document this is responding to)
 * responses (list/array)
 
    * value (integer, boolean, or text)
    * survey_document.question
    
 * user_id (used to relate to SQL)
 * survey_id (used to relate to SQL)
 * survey_state_id (used to relate to SQL)
    