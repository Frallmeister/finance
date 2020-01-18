# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:02:47 2020

@author: Fredrik

"""

import os
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt



class MyEconomy:
    
    def __init__(self,
                 filename,
                 start_capital=None,
                 start_date=None,
                 stop_date=None,
                 ):
        
        if start_date and stop_date:
            assert start_date < stop_date, "start_date must be earlier than stop_date."
            
            
        #self.dividend = 0 if dividend==None else dividend
        
        self.start_date = start_date
        self.stop_date = stop_date
        #self.monthly_start = monthly_start
        #self.monthly_stop = monthly_stop
        
        self.read_csv(filename)
        
        
    def read_csv(self, filename):
        
        self.dates = []
        self.close = []
        
        with open(filename, 'r') as csv_file:
            
            csv_reader = csv.reader(csv_file, delimiter=";")
            
            # Skip first two lines
            next(csv_reader)
            next(csv_reader)
            
            for row in csv_reader:
                self.dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d").date())
                self.close.append(float(row[3].replace(' ', '').replace(',', '.')))
                
                # Fill close = 0 with previous value
                if self.close[-1] == 0:
                    self.close[-1] = self.close[-2]
                    
            # Reverse the lists to obtain ascending dates
            self.dates.reverse()
            self.close.reverse()
        
        
        def run(self, start_capital=None, month_save=None,
                monthly_start=None, monthly_stop=None):
            
            capital = 0 if start_capital==None else start_capital
            
            if monthly_start and monthly_stop:
                assert monthly_start < monthly_stop, "monthly_start must be earlier than monthly_stop."
            
            
        def sensitivity(self):
            pass



def main():
    f1 = "omxs30_GI_2020-01-17.csv"
    f2 = "omxs30_1990_2019.csv"
    a = MyEconomy("src/" + f2)
    return a

if __name__ == '__main__':
    a = main()