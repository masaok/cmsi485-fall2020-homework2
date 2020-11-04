#!/usr/bin/env python3

from pomegranate import *
import numpy as np
import pandas as pd

'''
warmup.py

Skeleton for answering warmup questions related to the
AdAgent assignment. By the end of this section, you should
be familiar with:
- Importing, selecting, and manipulating data using Pandas
- Creating and Querying a Bayesian Network
- Using Samples from a Bayesian Network for Approximate Inference

@author: <Your Name(s) Here>
'''

if __name__ == '__main__':
    """
    PROBLEM 2.1
    Using the Pomegranate Interface, determine the answers to the
    queries specified in the instructions.
    
    ANSWER GOES BELOW:
    """
    
    # TODO: 2.1

    data = pd.read_csv("./dat/adbot-data.csv")

    print(data)
    print(data.columns)

    model = BayesianNetwork.from_samples(X=data, algorithm='exact', state_names=data.columns)

    print(model.predict_proba({}))
    results = model.predict_proba({})

    p_s_query_result = results[5].parameters[0]  # query result for P(S)
    print(p_s_query_result)

    results = model.predict_proba({'G': 1})

    p_s_query_result = results[5].parameters[0]  # query result for P(S|G=1)
    print(p_s_query_result)

    results = model.predict_proba({'T': 1, 'H': 1})

    p_s_query_result = results[5].parameters[0]  # query result for P(S|T=1,H=1)
    print(p_s_query_result)

    # return
    
