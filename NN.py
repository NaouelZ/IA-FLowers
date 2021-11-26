# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:16:22 2021

@author: meric
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import pathlib
from tensorflow import keras
from keras.models import model_from_json
from tensorflow.keras.models import Sequential
import init



batch_size = 32
img_height = 180
img_width = 180



json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']


def test_model(fname):
    
    path = "./static/"+fname
    image = tf.keras.preprocessing.image.load_img(path, target_size = (180,180))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    #os.remove(path)
    
    
    tensor = tf.expand_dims(image, 0) 
    
    predictions = loaded_model.predict(tensor)
    score = tf.nn.softmax(predictions[0])
    
    res = "Cette fleur est une {} avec une certitude de {:.2f} %.".format(class_names[np.argmax(score)], 100 * np.max(score))
    
    return res
  