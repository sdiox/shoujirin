#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'sdiox'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class KeywordForm(Form):
    keyword = StringField('', validators=[DataRequired()])
    onlyFirstPage = BooleanField('only first page', validators=[DataRequired()], default=True)
    submit = SubmitField('Search')
