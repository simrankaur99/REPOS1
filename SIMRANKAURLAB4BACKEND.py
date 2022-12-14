#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template

app=Flask(_name_)
pickle_input = open("SIMRANKAUR_model.pkl","rb")
random_forest_model = pickle.load(pickle_input)
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=["POST"])
def predict():
    input_feat = [x for x in request.form.values()]
    final_model_features = [np.array(input_feat)]
    preds = random_forest_model.predict(final_model_features)
    return render_template('index.html', prediction_text = 'The species that the fish belongs to is {}'.format(str(preds)))

if _name=='main_':
    app.run(host='0.0.0.0',debug=True,port=port)

