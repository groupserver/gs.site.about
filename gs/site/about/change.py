# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import SiteForm
from gs.content.form.base.wymeditor import wym_editor_widget
from gs.content.form.base.utils import enforce_schema
from Products.XWFCore.XWFUtils import get_the_actual_instance_from_zope
from .audit import ChangeAuditor, CHANGE
from .interfaces import ISiteIntro


class Change(SiteForm):
    label = 'Change about'
    pageTemplateFileName = 'browser/templates/change.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(ISiteIntro, render_context=True)

    def __init__(self, context, request):
        super(Change, self).__init__(context, request)
        enforce_schema(context, ISiteIntro)
        self.form_fields['introduction'].custom_widget = \
            wym_editor_widget

    @form.action(label='Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        ctx = get_the_actual_instance_from_zope(self.context)
        form.applyChanges(ctx, self.form_fields, data)
        auditor = ChangeAuditor(ctx)
        auditor.info(CHANGE, str(len(data['introduction'])))
        self.status = ('The introduction text that appears on '
                       '<a href="/">the site homepage</a> has been '
                       'changed.')

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
