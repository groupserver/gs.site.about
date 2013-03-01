# coding=utf-8
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.form import SiteForm
from gs.content.form.utils import enforce_schema
from gs.content.form.wymeditor import wym_editor_widget
from Products.XWFCore.XWFUtils import get_the_actual_instance_from_zope
from interfaces import ISiteIntro
from audit import ChangeAuditor, CHANGE


class Change(SiteForm):
    label = u'Change About'
    pageTemplateFileName = 'browser/templates/change.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(ISiteIntro, render_context=True)

    def __init__(self, context, request):
        SiteForm.__init__(self, context, request)
        enforce_schema(context, ISiteIntro)
        self.form_fields['introduction'].custom_widget = \
            wym_editor_widget

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        ctx = get_the_actual_instance_from_zope(self.context)
        form.applyChanges(ctx, self.form_fields, data)
        auditor = ChangeAuditor(ctx)
        auditor.info(CHANGE, str(len(data['introduction'])))
        self.status = u'The introduction text that appears on '\
                        u'<a href="/">the site homepage</a> has been '\
                        u'changed.'
        assert type(self.status) == unicode

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode
