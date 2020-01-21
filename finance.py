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
    
    def __init__(self, filename):
        
        # Read in dates and close from filename
        self.read_csv(filename)
        
        
    def read_csv(self, filename):
        
        self.dates = []
        self.close = []
        
        with open(filename, 'r') as csv_file:
            
            csv_reader = csv.reader(csv_file, delimiter=";")
            
            # Skip first two lines
            next(csv_reader)
            next(csv_reader)
            
            # Get Close and dates from csv_reader
            for row in csv_reader:
                self.dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d").date())
                self.close.append(float(row[3].replace(' ', '').replace(',', '.')))
                
                # Fill close = 0 with previous value
                if self.close[-1] == 0:
                    self.close[-1] = self.close[-2]
                    
            # Reverse the lists to obtain ascending dates
            self.dates.reverse()
            self.close.reverse()
        
        
    def run(self,
            start_capital=None,
            monthly_save=None,
            monthly_start=None,
            monthly_stop=None,
            start_date=None,
            stop_date=None,
            dividend=None):
        
        # Raise errors for inputs not allowed.
        if start_date and stop_date:
            assert start_date < stop_date, "start_date must be earlier \
                than stop_date."
            
        if not monthly_save and (monthly_start or monthly_stop):
            raise Exception("Start or stop date for monthly saving \
                            defined without saving ammount")
        
        if monthly_start and monthly_stop:
            assert monthly_start < monthly_stop, "monthly_start must be \
                earlier than monthly_stop."
                

        capital = 0 if start_capital==None else start_capital
        dividend = 0 if dividend==None else dividend
        monthly_save = 0 if monthly_save==None else monthly_save
        
        start_date = self.dates[0] if start_date==None else start_date
        stop_date = self.dates[-1] if stop_date==None else stop_date
        
        monthly_start = start_date if monthly_start==None else monthly_start
        monthly_stop = stop_date if monthly_stop==None else monthly_stop
        
        # Determine start index for the loop below
        #if start_date:
        tmp = [start_date >= d for d in self.dates]
        ind_start_date = tmp.index(True)
        #else:
        #    ind_start_date = 0
            
        # Determine stop index for the loop below
        #if stop_date:
        tmp = [stop_date <= d for d in self.dates]
        ind_stop_date = tmp.index(True)
        #else:
        #    ind_stop_date = len(a.dates)
            
        self.capital = [capital]
        self.profit = [0]
        self.invested = 0
        # Loop over dates and close to calculate capital
        for i in range(ind_start_date, ind_stop_date):
            
            # Capital growth from index
            next_day = self.capital[-1]*self.close[i+1]/self.close[i]
            
            # Add monthly savings on first trade day of the month
            if self.dates[i] >= monthly_start and \
               self.dates[i] <= monthly_stop and \
               self.dates[i+1].month > self.dates[i].month:
                next_day += monthly_save
                self.invested += monthly_save
                
            # Add dividend to capital on the first day in April
            if self.dates[i+1].month==4 and self.dates[i].month==3:
                next_day += self.capital[-1] * dividend/100
            
            # Append next days calculated capital to the capital attribute.
            self.capital.append(next_day)
            self.profit.append(next_day-capital-self.invested)
            
            
        def sensitivity(self, start_capital, monthly_save, rate):
            
            pass

# TODO: case when provided start_date is earlier than first date in the csv.

def main():
    f1 = "omxs30_GI_2020-01-17.csv"
    f2 = "omxs30_1990_2019.csv"
    f3 = "OMXSBCAPGI_1996_2020.csv"
    money = MyEconomy("src/" + f3)
    
    money.run(start_capital=500000,
          start_date=datetime.date(1995,12,31),
          #monthly_start=datetime.date(1990,9,1),
          #monthly_stop=datetime.date(2006,8,1),
          monthly_save=5000,)
    return money

if __name__ == '__main__':
    a = main()