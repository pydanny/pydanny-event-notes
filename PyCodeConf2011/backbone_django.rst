====================
Backbone.js + Django
====================

* by Leah Culver

* Works at convore.com, a YC Combinator funded project
* LeafyChat - Django Dash 2009
* web-based IRC client

Convore issue?
--------------

* Who is supposed to use it?
* Internal company stuff
* What kind of discussions

Grove!
--------------

* IRC for your company
* Internal for companies
* https://grove.io 

Leafy Chat
--------------

* Pure JavaScript
* very barebones - just JQuery
* Very dirty in that their construct HTML manually

Each submit for chat:

1. handle form submit
2. create new message
3. display mesage in list
4. POST method in AJAX

Backbone!
----------

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

.. sourcecode:: python

    def python_here