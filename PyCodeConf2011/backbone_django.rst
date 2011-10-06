====================
Backbone.js + Django
====================

.. note:: I'm having trouble keeping up when it comes to writing JS fast. :P

* by Leah Culver
* Works at convore.com, a YC Combinator funded project
* LeafyChat - Django Dash 2009
* web-based IRC client

Convore issue?
==============

* Who is supposed to use it?
* Internal company stuff
* What kind of discussions

Grove!
==============

* IRC for your company
* Internal for companies
* https://grove.io 

Leafy Chat
==============

* Pure JavaScript
* very barebones - just JQuery
* Very dirty in that their construct HTML manually

Each submit for chat:

1. handle form submit
2. create new message
3. display mesage in list
4. POST method in AJAX

Backbone!
==============

* MVC style of programming for AJAX/JavaScript
* More like DJango: MTV

.. sourcecode:: javascript

    // models are easy!
    window.Message = Backbone.model.extend({
        model: Message,
        
        initialize: function(){
            this.model.bind('add', this.addMessage)
            // TODO 
        
        },        
        
        });
        
    // form submits
    submitForm: function(){
        
    
    };


Handlebars templates
==============

* handlebars.js templates
* looks like Django/Jinja2 templates
* Why not JQuery templates?
* See include_raw template tag as per htto://djangosnippets.org/snippets/1684

Addition Goodies about backbone.js
================================================

* Uses similiar routing to Django
* Handy code snippet by Leah for Django CBV usage:

    * https://gist.github.com/1265346

* Event based asynchronous

    * One thing can fire off multiple request
    * So if I am watching and someone else posts then I see the results

Router
=======

 * Can do overlaps of views