# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:59:53 2021

@author: Pavithra
"""

from tensorflow.contrib import lite
converter = lite.TFLiteConverter.from_keras_model_file( 'rockpaperscissor-model.h5' ) # Your model's name
model = converter.convert()
file = open( 'rockpaperscissor-model.tflite' , 'wb' ) 
file.write( model )