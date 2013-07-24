# -*- coding: utf-8 -*-
from zope.interface.interface import Interface
from zope.schema import Text
from zope.viewlet.interfaces import IViewletManager


class ISiteIntro(Interface):
    introduction = Text(title=u'Introduction Text',
                    description=u'The text that you want to see on the site '
                        u'homepage.',
                    required=True)


class IGSSiteHomeAbout(IViewletManager):
    u'''The About text that appears on the site homepage'''
