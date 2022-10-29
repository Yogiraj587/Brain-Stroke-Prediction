import pickle
from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open('ML/Brain Stroke Prediction/model.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")
