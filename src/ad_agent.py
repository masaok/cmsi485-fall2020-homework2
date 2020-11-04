#!/usr/bin/env python3

'''
ad_engine.py
Advertisement Selection Engine that employs a Decision Network
to Maximize Expected Utility associated with different Decision
variables in a stochastic reasoning environment.

@author: <Your Name(s) Here>
'''
import pandas as pd
from pomegranate import *
import math
import itertools
import unittest


class AdEngine:

    def __init__(self, data_file, dec_vars, util_map):
        """
        Responsible for initializing the Decision Network of the
        AdEngine using the following inputs
        
        :param string data_file: path to csv file containing data on which
        the network's parameters are to be learned
        :param list dec_vars: list of string names of variables to be
        considered decision variables for the agent. Example:
          ["Ad1", "Ad2"]
        :param dict util_map: discrete, tabular, utility map whose keys
        are variables in network that are parents of a utility node, and
        values are dictionaries mapping that variable's values to a utility
        score, for example:
          {
            "X": {0: 20, 1: -10}
          }
        represents a utility node with single parent X whose value of 0
        has a utility score of 20, and value 1 has a utility score of -10
        """
        # TODO! You decide the attributes and initialization of the network!

        data = pd.read_csv(data_file)

        print(data)
        # print(data.columns)

        self.model = BayesianNetwork.from_samples(X=data, algorithm='exact', state_names=data.columns)
        results = self.model.predict_proba({ 'X': 0, 'D': 0 })


        self.var_vals = dict()

        print("INIT > LOOP:")
        for item in data.columns:
            print(item)
            arr = data[item].unique()
            print(arr)
            self.var_vals[item] = arr.tolist()

        print(self.var_vals)

        print("INIT > RESULTS:")
        print(results)

        self.dec_vars = dec_vars
        self.util_map = util_map

        return
        

    def eu(self, action, evidence):
        print("FUNCTION > EU... ")

        print("FUNCTION > EU > action: ")
        print(action)

        print("FUNCTION > EU > evidence: ")
        print(evidence)

        print("FUNCTION > EU > util_map: ")
        print(self.util_map)

        results = self.model.predict_proba({ 'D': 0 })

        for val in self.var_vals[action]:
          print("LOOP VAL:")
          print(val)

        # for 


    def meu(self, evidence):
        """
        Given some observed demographic "evidence" about a potential
        consumer, selects the ad content that maximizes expected utility
        and returns a dictionary over any decision variables and their
        best values plus the MEU from making this selection.
        
        :param dict evidence: dict mapping network variables to their
        observed values, of the format: {"Obs1": val1, "Obs2": val2, ...}
        :return: 2-Tuple of the format (a*, MEU) where:
          - a* = dict of format: {"DecVar1": val1, "DecVar2": val2, ...}
          - MEU = float representing the EU(a* | evidence)
        """
        # TODO: Implement the above!



        action = self.dec_vars

        self.eu(action, evidence)

        best_decisions, best_util = dict(), -math.inf
        return (best_decisions, best_util)


    def vpi(self, potential_evidence, observed_evidence):
        """
        Given some observed demographic "evidence" about a potential
        consumer, returns the Value of Perfect Information (VPI)
        that would be received on the given "potential" evidence about
        that consumer.
        
        :param string potential_evidence: string representing the variable name
        of the variable under evaluation
        :param dict observed_evidence: dict mapping network variables 
        to their observed values, of the format: {"Obs1": val1, "Obs2": val2, ...}
        :return: float value indicating the VPI(potential | observed)
        """
        # TODO: Implement the above!
        return 0
        

class AdAgentTests(unittest.TestCase):
    
    def test_meu_lecture_example_no_evidence(self):
        ad_engine = AdEngine('../dat/lecture5-2-data.csv', ["D"], {"Y": {0: 3, 1: 1}})
        evidence = {}
        decision = ad_engine.meu(evidence)
        self.assertEqual({"D": 0}, decision[0])
        self.assertAlmostEqual(2, decision[1], delta=0.01)
    
    # def test_meu_lecture_example_with_evidence(self):
    #     ad_engine = AdEngine('../dat/lecture5-2-data.csv', ["D"], {"Y": {0: 3, 1: 1}})
    #     evidence = {"X": 0}
    #     decision = ad_engine.meu(evidence)
    #     self.assertEqual({"D": 1}, decision[0])
    #     self.assertAlmostEqual(2, decision[1], delta=0.01)
        
    #     evidence2 = {"X": 1}
    #     decision2 = ad_engine.meu(evidence2)
    #     self.assertEqual({"D": 0}, decision2[0])
    #     self.assertAlmostEqual(2.4, decision2[1], delta=0.01)
        
    # def test_vpi_lecture_example_no_evidence(self):
    #     ad_engine = AdEngine('../dat/lecture5-2-data.csv', ["D"], {"Y": {0: 3, 1: 1}})
    #     evidence = {}
    #     vpi = ad_engine.vpi("X", evidence)
    #     self.assertAlmostEqual(0.24, vpi, delta=0.1)
    
    # def test_meu_defendotron_no_evidence(self):
    #     ad_engine = AdEngine('../dat/adbot-data.csv', ["Ad1", "Ad2"], {"S": {0: 0, 1: 1776, 2: 500}})
    #     evidence = {}
    #     decision = ad_engine.meu(evidence)
    #     self.assertEqual({"Ad1": 1, "Ad2": 0}, decision[0])
    #     self.assertAlmostEqual(746.72, decision[1], delta=0.01)
        
    # def test_meu_defendotron_with_evidence(self):
    #     ad_engine = AdEngine('../dat/adbot-data.csv', ["Ad1", "Ad2"], {"S": {0: 0, 1: 1776, 2: 500}})
    #     evidence = {"T": 1}
    #     decision = ad_engine.meu(evidence)
    #     self.assertEqual({"Ad1": 1, "Ad2": 1}, decision[0])
    #     self.assertAlmostEqual(720.73, decision[1], delta=0.01)
        
    #     evidence2 = {"T": 0, "G": 0}
    #     decision2 = ad_engine.meu(evidence2)
    #     self.assertEqual({"Ad1": 0, "Ad2": 0}, decision2[0])
    #     self.assertAlmostEqual(796.82, decision2[1], delta=0.01)
        
    # def test_vpi_defendotron_no_evidence(self):
    #     ad_engine = AdEngine('../dat/adbot-data.csv', ["Ad1", "Ad2"], {"S": {0: 0, 1: 1776, 2: 500}})
    #     evidence = {}
    #     vpi = ad_engine.vpi("G", evidence)
    #     self.assertAlmostEqual(20.77, vpi, delta=0.1)
        
    #     vpi2 = ad_engine.vpi("F", evidence)
    #     self.assertAlmostEqual(0, vpi2, delta=0.1)
        
    # def test_vpi_defendotron_with_evidence(self):
    #     ad_engine = AdEngine('../dat/adbot-data.csv', ["Ad1", "Ad2"], {"S": {0: 0, 1: 1776, 2: 500}})
    #     evidence = {"T": 0}
    #     vpi = ad_engine.vpi("G", evidence)
    #     self.assertAlmostEqual(25.49, vpi, delta=0.1)
        
    #     evidence2 = {"G": 1}
    #     vpi2 = ad_engine.vpi("P", evidence2)
    #     self.assertAlmostEqual(0, vpi2, delta=0.1)
        
    #     evidence3 = {"H": 0, "T": 1, "P": 0}
    #     vpi3 = ad_engine.vpi("G", evidence3)
    #     self.assertAlmostEqual(66.76, vpi3, delta=0.1)
        
if __name__ == '__main__':
    unittest.main()
