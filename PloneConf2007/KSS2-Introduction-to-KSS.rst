============================================
Introduction to KSS, Kinetic Style Sheets
============================================

.. note:: Before JQuery let me walk the dom effortlessly, I had grown annoyed with JavaScript. I didn't know then it was the DOM, and not the language. KSS seemed like a solution - *because CSS syntax against DOM agony is better than JavaScript syntax against DOM agony*? In any case, Plone later introduced JQuery and I hope KSS is out. (Danny 07/05/2011)

by Balazs Ree
=========================

http://kssproject.org/docs/tutorials/simple-kss
http://codespeak.net/svn/kukit/docs/introducing_kss/trunk

get FireKSS for firefox. Then do stuff like:

.. sourcecode:: css

    h2: click	{
        action-click: alert;
    }

    h2: click	{
        action-click: setStyle;
        setStyle-node:	backgroundColor;
    }