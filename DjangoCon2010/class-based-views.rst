=================
Class based views
=================

by Ben Firshman


Views have not been updated since release of Django
Generic views are very inflexible
newforms-admin use class based views

In the request -- views -- reponse stream a view is just a callable (__call())

Class based views let you do mixins such as rendering Jinja or JSON values.  This beats Piston,
TastyPie, etc by letting you not have to create a separate application framework.