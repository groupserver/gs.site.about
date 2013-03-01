# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import Text


class ISiteIntro(Interface):
    introduction = Text(title=u'Introduction Text',
                    description=u'The text that you want to see on the site '
                        u'homepage.',
                    required=True)
