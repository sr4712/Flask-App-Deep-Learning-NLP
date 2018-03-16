#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classes for sensitivity analysis.
"""
import os
import pandas as pd
from bokeh.plotting import figure


class DF_Loader:
    
    '''Loads required objects to perform sensitivity analysis.
    
    
    # Arguments:
        df_sensitivity_path: filepath for directory containing 
            dataframes with sensitivity analysis results
        
    '''
    
    def __init__(self, df_sensitivity_path):
        self.df_sensitivity_path = df_sensitivity_path

    def return_filenames(self):
        filenames = list(os.walk(self.df_sensitivity_path))[0][2]
        return filenames
        
    def pickle_df_sens_loader(self):
        filenames = self.return_filenames()
        dict_sens_df = {x.replace('.pickle',''): pd.read_pickle(self.df_sensitivity_path + '/' + x) for x in filenames}
        return dict_sens_df


class Plotter():
    
    '''Creates interactives Bokeh plots
    
    
    # Arguments:
        df_plot: dataframe containing sensitivity analysis results
        plot_title: desired title for the plot
        param_feature_name: feature name for the independent tuning parameter
        acc_feature_name: featuer name for the dependent metric
        
    '''
    
    def __init__(
            self,
            df_plot,
            plot_title,
            param_feature_name,
            acc_feature_name):
        
        self.df_plot = df_plot
        self.plot_title = plot_title
        self.param_feature_name = param_feature_name
        self.acc_feature_name = acc_feature_name 
        
    def create_plot(self):
        plot_tools = "pan,hover, wheel_zoom,box_zoom,reset,save,box_select"
        sensitivity_plot = figure(
                                  title=self.plot_title,
                                  tools=plot_tools,
                                  plot_width=400,
                                  plot_height=400)
        sensitivity_plot.line(
                             self.df_plot[self.param_feature_name],
                             self.df_plot[self.acc_feature_name],
                             line_width=2)
        sensitivity_plot.circle(
                               self.df_plot[self.param_feature_name],
                               self.df_plot[self.acc_feature_name],
                               fill_color="black",
                               size=8)
        
        sensitivity_plot.xgrid.grid_line_color = None
        sensitivity_plot.ygrid.grid_line_color = None
        return sensitivity_plot        