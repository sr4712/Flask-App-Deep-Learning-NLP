#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Please input your review to perform sentiment analysis.', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SensitivityForm(FlaskForm):
    select_field = SelectField('Select Tuning Parameter', choices=[], default = 'sensitivity_analysis_sequence_length_df' )
    submit = SubmitField('Go')    
    
    
    
