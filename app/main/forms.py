#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import settings


class NameForm(FlaskForm):
    name = StringField(
            'Please input your review to perform sentiment analysis.',
            validators=[DataRequired()]
            )
    submit = SubmitField('Submit')


class SensitivityForm(FlaskForm):
    select_field = SelectField(
            'Select Tuning Parameter',
            choices=[],
            default = settings.DEFAULT_SENSITIVITY_ANALYSIS_DF)
    submit = SubmitField('Go')    
    
    
    
