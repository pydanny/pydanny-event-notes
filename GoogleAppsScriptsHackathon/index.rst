============================
Google Apps Script Hackathon
============================

https://sites.google.com/site/appsscripthackathonlosangeles/

What is Apps Script?
=====================

Google Apps Script is a JavaScript cloud scripting language that provides easy ways to automate with Google products. Started in the spreadsheets and was expanded from there.

see http://www.google.com/script/start/

Features
---------

* Editor in the browser
* Works with spreadsheets
* Sending email
* JDBC connector
* XML parsing
* SOAP
* Make HTTP requests with URLfetch
* Outbound OAuth support
* Build custom UIs
* Run script as a serice

Use Cases
===========

Grading made easy with Flubaroo
--------------------------------

* Create quiz using google forms
* Automatically grades against answer key
* Can email results and answers to each student
* Provides charts to analyze the results

Many types of mail merge
------------------------

* Define a template
* Mail!

Vacation calendar for Brown University
----------------------------------------

* Aggregates staff that are on vacation
* Displays the results in a calendar instance

Sample code snippets
====================

.. code-block:: javascript

    function emailTest() {
      // Send myself an email
      MailApp.sendEmail("pydanny@gmail.com", "LA Hackathon test email", "Body of email"); 
  
      // Get a list of my files with 'Django' in it
      var files = DocsList.find("Django");
  
      // Loop and log
      for (var i in files){
        Logger.log(i + '-----------');
        Logger.log(files[i].getId());
      }
  
      //var app = UiApp.createApplication();
    }


My createHomePage code
======================

This is my implementation of https://developers.google.com/apps-script/articles/sites_tutorial. It uses a mix of Contacts,
Calendar, and Sites to generate a page tracking IRC discussions.

Unfortunately the problem is that the tutorial seems to have fallen behind the current API. Took me a while to hack this to work.



.. code-block:: javascript


      // create a new site
  
      // ISSUE: had to grab existing site because SitesApp.createSite throws strange errors
      var site = SitesApp.getSiteByUrl("https://sites.google.com/site/pydanny/");

      // add team members from our Gmail Contacts as collaborators, and create a profile webpage for each contact
      var contacts = ContactsApp.findContactGroup("Python").getContacts();
      for (var i = 0; i < contacts.length; i++) {
    
        // ISSUE: Did this because the first item is a title field of 'contact'
        if (i===0){
          continue;
        };

        try {
          site.addCollaborator(contacts[i].getPrimaryEmail()); 
  
          var name = contacts[i].getFullName();
          var pageName = name.replace(/\s/g,"");
          var phone = contacts[i].getWorkPhone();
          var description = contacts[i].getNotes();
        } catch(e){};

        var welcomeMessage = name + "'s profile page<br/><br/>Phone: " + phone + "<br/><br/>" + description;
        try {    
          // ISSUE: Did this because on additional runs this for people withpages it throws errors
          var webpage = site.createWebPage(name + "'s Page", pageName + "sPage", welcomeMessage);
        } catch(e){};      
      }

      // notify club members about future matches
  
      // TODO: Make this work by trying site.getChildByName and then site.createAnnouncementsPage
      try {  
        var annPage = site.createAnnouncementsPage("PyCon Annoucements", "Announcements", "New announcements for the PyCon thunderdome team will be posted here.");
      } catch(e){
        var annPage = site.getChildByName("Annoucements");
      };   
      var d1 = new Date("10/20/2012");
      var d2 = new Date("12/30/2012");
      var events = CalendarApp.openByName("Daniel Greenfeld").getEvents(d1, d2);
      for (var i = 0; i < events.length; i++) {
        var message = "<p>There will be a thunderdome chat from " + events[i].getStartTime() + " until " + events[i].getEndTime() + "!</p>";
        var count = i + 1;    
        var notice = "Thunderdome Chat #" + count
        Logger.log(count);    
        Logger.log(message);
    
        // ISSUE: No easy way to check if an announcement has already been created
        try {      
          annPage.createAnnouncement(notice, message);
        } catch(e){};
      }
    }