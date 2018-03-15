#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.models import load_model
from keras.preprocessing import sequence
import re
import pickle


class Loader:    
    def __init__(self, model_path, word_to_index_dict_path, index_to_word_dict_path):
        self.model_path = model_path
        self.word_to_index_dict_path = word_to_index_dict_path
        self.index_to_word_dict_path = index_to_word_dict_path  
                
    def model_loader(self):
        try:
            model = load_model(self.model_path)
            return model
        except Exception as err:
            print('Error loading model:', err)
                      
    def word_to_index_dict_loader(self):
        try:
            pickle_input = open(self.word_to_index_dict_path, 'rb')
            word_to_index_dict = pickle.load(pickle_input)
        except Exception as err:
            print('Error loading word to index dictionary:', err)            
        return word_to_index_dict
    
    def index_to_word_dict_loader(self):
        try:
            pickle_input = open(self.index_to_word_dict_path, 'rb')
            index_to_word_dict = pickle.load(pickle_input)
        except Exception as err:
            print('Error loading index to word dictionary:', err)            
        return index_to_word_dict
    
    
class Model_Predictor:
    def __init__(self, loader, unknown_token, start_token, sequence_length):    
        self.loader = loader
        self.unknown_token = unknown_token
        self.start_token = start_token
        self.sequence_length = sequence_length
       
    def preprocess_input(self,sentence_input):
        words_input=sentence_input.split()
        words_input=[re.sub(r'[^\w\s]','',x) for x in words_input ]                    
        words_input = words_input * 20
        return words_input
                
    def prepare_input_sentence_for_prediction(self,sentence_input):
        words_input = self.preprocess_input(sentence_input)
        word_to_index_dict = self.loader.word_to_index_dict_loader()
        
        predict_sentence =  [word_to_index_dict[self.start_token]]                  #add the start token
                                                        
        for index_word in words_input:
            if index_word in word_to_index_dict:
                next_seq=word_to_index_dict[index_word]
            else:
                next_seq= word_to_index_dict[self.unknown_token]    
            predict_sentence.append(next_seq)   
    
        predict_sentence=sequence.pad_sequences([predict_sentence],maxlen=self.sequence_length,padding='post',truncating='post',value=0)             
        return(predict_sentence)

    def initialise_model(self):
        global sa_model
        sa_model = self.loader.model_loader()
        sa_model._make_predict_function()
    
    @staticmethod    
    def map_output_to_sentiment(model_output_probability):
        if model_output_probability >= .6:
            sa_result = 'Positive Sentiment'
        elif model_output_probability <= .4:
            sa_result = 'Negative Sentiment'
        else:
            sa_result = 'Model could not determine the sentiment. Please input a longer review'
        return sa_result    
                               
    def predict_with_model(self, sentence_input):
        self.initialise_model()
        sentence_input_for_model = self.prepare_input_sentence_for_prediction(sentence_input)
        model_output_probability = sa_model.predict(sentence_input_for_model)
        sa_result = self.map_output_to_sentiment(model_output_probability)
        return sa_result

