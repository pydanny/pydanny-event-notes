======================
Deprecated Features
======================

check out http://django.me/deprecation

Admin
=====

Don't use AdminSite.root()!

Follow this pattern::

    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls))
    )

Custom auth backends
=====================

New rules for anonymous users that must be in place::

    class MyAuthBackend(object):
        supports_object_permissions = False
        supports_anonymous_user = False
        supports_inactive_user = False
 