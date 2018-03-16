#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for
from bokeh.embed import components
from . import main
from .forms import SensitivityForm, NameForm
from ..model import Loader, Model_Predictor
from ..sensitivity_analysis import DF_Loader, Plotter
import settings


@main.route('/')
def index():
    return render_template('index.html')
        
@main.route('/model_output/predict', methods=['GET', 'POST'])
def model_predict():
    loader = Loader(
             settings.MODEL_PATH, 
             settings.WORD_TO_INDEX_DICT_PATH, 
             settings.INDEX_TO_WORD_DICT_PATH)
    model_predictor = Model_Predictor(
                      loader, 
                      settings.UNKNOWN_TOKEN,
                      settings.START_TOKEN, 
                      settings.SEQUENCE_LENGTH)
    
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        sa_model_output = model_predictor.predict_with_model(session['name'])
        session['sa_model_output'] = sa_model_output
        return redirect(url_for('.model_predict'))    
    return render_template(
                          'model_template.html', 
                          form=form, 
                          name='model in development. Please try again later')

@main.route('/sensitivity_analysis', methods=['GET', 'POST'])
def sensitivity_analysis():    
    df_loader = DF_Loader(settings.PLOT_DF_PATH)
    df_dict = df_loader.pickle_df_sens_loader()
    df_filenames = df_loader.return_filenames()
    form_choices = [(x.replace('.pickle','') , x.replace('.pickle','')) 
                    for x in df_filenames]
    
    form = SensitivityForm()
    form.select_field.choices = form_choices

    session['sens_param_choice'] = form.select_field.data        
    df_plot_input = df_dict[session['sens_param_choice']]    
    plotter = Plotter(
              df_plot_input, 
              settings.SENSITIVITY_PLOT_TITLE,
              settings.PARAM_FEATURE_NAME,
              settings.ACC_FEATURE_NAME)
    
    plot_sens = plotter.create_plot()    
    script, div = components(plot_sens)
    return render_template(
                           'sensitivity_analysis.html',
                           form=form,
                           script=script,
                           div=div)
   

    

    
