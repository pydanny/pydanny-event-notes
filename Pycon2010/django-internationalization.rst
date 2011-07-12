============================
Django Internationalization
============================

by Matt Croyden

*I already know all this thanks to most of my other Django work but I may learn something new*

Code
----------------

Sample code::

    from django.utils.translation import ugettext as _

    output = _("Hello, world!")
    
    
Translating models
------------------

 * Don't forget the Meta attributes!
 
 * All titles and help_text items on model attributes should be translated
 
Translating templates
------------------------

sample::

    {% load i18n %}
    {% block trans %}{% endblock trans %}
    {% trans "blah"%}

        
Its just Python
---------------

 * gettext, ugettext, ungettext are just simple wrappers around Python behavior
 
 * Django provides a lazy translation layer on top, useful in models and template tags/filters
 
