#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import dirname,  abspath


__dir__ = dirname(abspath(__file__))


MODEL_PATH = 'required_objects/sa_model.h5'
WORD_TO_INDEX_DICT_PATH = 'required_objects/word_to_index_dict.pickle'
INDEX_TO_WORD_DICT_PATH = 'required_objects/index_to_word_dict.pickle'
PLOT_DF_PATH = 'required_objects/sensitivity_df'

UNKNOWN_TOKEN = 'UNKNOWN_TOKEN'
START_TOKEN = 'START_TOKEN'
SEQUENCE_LENGTH = 400

SENSITIVITY_PLOT_TITLE = "Accuracy Vs. Tuning Parameter Values" 
PARAM_FEATURE_NAME = 'param_value'
ACC_FEATURE_NAME = 'y1'
DEFAULT_SENSITIVITY_ANALYSIS_DF = 'sensitivity_analysis_sequence_length_df'
