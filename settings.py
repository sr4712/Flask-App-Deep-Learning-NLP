#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define encoded settings used throughout application.
"""
from os.path import dirname,  abspath


__dir__ = dirname(abspath(__file__))


MODEL_PATH = 'required_objects/sa_model.hdf5'
WORD_TO_INDEX_DICT_PATH = 'required_objects/word_to_index_dict.pickle'
INDEX_TO_WORD_DICT_PATH = 'required_objects/index_to_word_dict.pickle'
PLOT_DF_PATH = 'required_objects/sensitivity_df'

UNKNOWN_TOKEN = 'unknown_token'
START_TOKEN = 'start_token'
SEQUENCE_LENGTH = 15

SENSITIVITY_PLOT_TITLE = "Val Accuracy Vs. Tuning Parameter Values" 
PARAM_FEATURE_NAME = 'param_value'
ACC_FEATURE_NAME = 'val_accuracy'
DEFAULT_SENSITIVITY_ANALYSIS_DF = 'sensitivity_analysis_max_words_df'
