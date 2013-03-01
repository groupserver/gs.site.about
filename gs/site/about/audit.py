# coding=utf-8
from datetime import datetime
from pytz import UTC
from zope.component import createObject
from zope.component.interfaces import IFactory
from zope.interface import implements
from Products.GSAuditTrail import IAuditEvent, BasicAuditEvent, \
    AuditQuery, event_id_from_data
from Products.CustomUserFolder.userinfo import userInfo_to_anchor
from Products.XWFCore.XWFUtils import munge_date

SUBSYSTEM = 'groupserver.SiteIntroduction'
import logging
log = logging.getLogger(SUBSYSTEM)

UNKNOWN = '0'
CHANGE = '1'


class ChangeAuditEventFactory(object):
    implements(IFactory)

    title = u'Change Site Introduction Audit-Event Factory'
    description = u'Creates a GroupServer audit event for changing '\
                    u'the site introduction.'

    def __call__(self, context, event_id, code, date,
        userInfo, instanceUserInfo, siteInfo, groupInfo=None,
        instanceDatum='', supplementaryDatum='', subsystem=''):

        if (code == CHANGE):
            event = ChangeEvent(context, event_id, date, siteInfo,
                        userInfo, instanceDatum)
        else:
            event = BasicAuditEvent(context, event_id, UNKNOWN, date,
              userInfo, None, siteInfo, None,
              instanceDatum, supplementaryDatum, SUBSYSTEM)
        assert event
        return event


class ChangeEvent(BasicAuditEvent):
    implements(IAuditEvent)

    def __init__(self, context, id, d, userInfo, siteInfo, instanceDatum):
        BasicAuditEvent.__init__(self, context, id, CHANGE, d, userInfo,
            None, siteInfo, None, instanceDatum, None, SUBSYSTEM)

    def __str__(self):
        retval = u'%s (%s) changed the site introduction text on %s '\
                    u'(%s). The introduction is now %s characters.' % \
                    (self.userInfo.name, self.userInfo.id,
                    self.siteInfo.name, self.siteInfo.id,
                    self.instanceDatum)
        return retval.encode('ascii', 'ignore')

    @property
    def xhtml(self):
        cssClass = u'audit-event site-event-%s' % self.code
        retval = u'<span class="%s">Change introduction</span>' % cssClass
        retval = u'%s &#8212; %s' % \
              (retval, userInfo_to_anchor(self.userInfo))
        retval = u'%s (%s)' % \
          (retval, munge_date(self.context, self.date))
        return retval


class ChangeAuditor(object):
    def __init__(self, site):
        self.site = site
        self.userInfo = createObject('groupserver.LoggedInUser', site)
        self.siteInfo = createObject('groupserver.SiteInfo', site)
        self.queries = AuditQuery()

        self.factory = ChangeAuditEventFactory()

    def info(self, code, instanceDatum=''):
        d = datetime.now(UTC)
        eventId = event_id_from_data(self.userInfo, self.userInfo,
                    self.siteInfo, code, instanceDatum, '')

        e = self.factory(self.site, eventId, code, d, self.userInfo,
                None, self.siteInfo, None, instanceDatum, None,
                SUBSYSTEM)

        self.queries.store(e)
        log.info(e)
