=================
``gs.site.about``
=================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The About box on a GroupServer Site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-06-19
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

This product provides the `About box`_ on the homepage of a GroupServer_
site, and the `Change page`_ to alter it.

About box
=========

The *About* box consists of three components: 

#. The box itself, a viewlet called ``gs-site-about-home``,
#. The content of the box, ``gs-site-about-home-content``,
#. A link from the box to the `Change page`_,
   ``gs-site-about-home-change``,

The contents of the *About* box comes from the ``introduction`` property of
the site-folder.

Change page
===========

The *Change About* page ``/admin_changeintro.html`` is also provided by
this product. It changes the ``introduction`` property of the site-folder,
which is then used by the `About box`_.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.site.about/
- Questions and comments to http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _GroupServer.org: http://groupserver.org/
.. _GroupServer: http://groupserver.org/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
.. _browser resource: http://docs.zope.org/zope.browserresource/
.. _OnlineGroups.Net: http://onlinegroups.net/
