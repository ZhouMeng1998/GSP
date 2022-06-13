# from ast import pattern
import logging
import random
from unittest import TestCase
import csv
from csv import reader
import nltk
import pandas as pd
from sqlalchemy import column
# from apyori import apriori
from efficient_apriori import apriori
import random
import matplotlib.pyplot as plt


from gsppy.gsp import GSP

logging.basicConfig(level=logging.DEBUG)


class TestGSP(TestCase):
    @staticmethod
    def create_transactions(minsize, maxsize, minvalue, maxvalue):
        return [random.randint(minvalue, maxvalue)
                for _ in range(random.randint(minsize, maxsize))]

    def test_artificial_transactions(self):
        minsize, maxsize, minvalue, maxvalue = 2, 256, 0, 5

        transactions = [TestGSP.create_transactions(
            minsize, maxsize, minvalue, maxvalue) for _ in range(10)]

        result = GSP(transactions).search(0.3)

        # print("========= Status =========")
        # print("Transactions: {}".format(transactions))
        print("GSP: {}".format(result))

    def test_supermarket(self):
        transactions = [
            ['Bread', 'Milk'],
            ['Bread', 'Diaper', 'Beer', 'Eggs'],
            ['Milk', 'Diaper', 'Beer', 'Coke'],
            ['Bread', 'Milk', 'Diaper', 'Beer'],
            ['Bread', 'Milk', 'Diaper', 'Coke']
        ]

        result = GSP(transactions).search(0.3)
        final = [{('Bread',): 4, ('Diaper',): 4, ('Milk',): 4, ('Beer',): 3, ('Coke',): 2},
                 {('Bread', 'Milk'): 3, ('Diaper', 'Beer'): 3, ('Milk', 'Diaper'): 3},
                 {('Bread', 'Milk', 'Diaper'): 2, ('Milk', 'Diaper', 'Beer'): 2}]
        print("========= Status =========")
        print("Transactions: {}".format(transactions))
        print("GSP: {}".format(result))

        self.assertEquals(result, final)










    def test_tweetsExperiments(self):
        with open('clean_covid_500.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
            print(list_of_rows)

        
        transactions = []

        for row in list_of_rows:
            c = ' '.join(row)
            a = c.split(',')
            transactions.append(a)

        result = GSP(transactions).search(0.05)  #for 100 tweets 0.02 too slow  0.04 too quick 0.03 seems fine
        print("========= Status =========")
        # print("Transactions: {}".format(transactions))
        print("GSP: {}".format(result))
        # association_rules = apriori(transactions, min_support=0.03, min_confidence=0.2, min_lift=3, min_length=2)
        # association_results = list(association_rules)
        # print(association_results)
        # for r in association_results:
        #     print(r)
        itemsets, rules = apriori(transactions, min_support=0.05, min_confidence=0.3)
        
        # visualize support and confidence
        confidence = []
        support = []
        for r in rules:
            if r.lift >= 3:
                print(r)
                sup = r.support + 0.0025 * (random.randint(1,10) - 5) 
                conf = r.confidence + 0.0025 * (random.randint(1,10) - 5)
                confidence.append(conf)
                support.append(sup)
        plt.scatter(support, confidence,   alpha=0.5, marker="*")
        plt.xlabel('support')
        plt.ylabel('confidence') 
        plt.show()
        #visualize support
        for r in result:
            plt.barh(range(len(r)), r.values(), align='center')
        plt.show()




