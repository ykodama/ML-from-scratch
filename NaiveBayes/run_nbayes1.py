#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NaiveBayes1 test runner

Chapter "Naive Bayes: a Primary Course"
"""

# imports
import numpy as np
from nbayes1 import NaiveBayes1

# load data
data = np.genfromtxt('vote_filled.tsv', dtype=np.int)

# split data
X = data[:, :-1]
y = data[:, -1]

# learn model
clr = NaiveBayes1()
clr.fit(X, y)

# test model
predict_y = clr.predict(X[:10, :])

# print results
for i in xrange(10):
    print i, y[i], predict_y[i]
