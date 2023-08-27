#!/usr/bin/env python

import pandas as pd
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import LogisticRegression
import shap
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import importlib.util
from abstract_model import AbstractModel

class Model(AbstractModel):
    def __init__(self):
        self.model = self.model_definition()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def predict_proba(self, X_test):
        return self.model.predict_proba(X_test)

    def get_params(self):
        return self.model.get_params()


    def model_definition(self):
        clf = LogisticRegression(penalty='l1', solver='liblinear',
                                 random_state=12345)
        return clf

