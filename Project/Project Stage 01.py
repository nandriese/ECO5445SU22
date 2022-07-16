# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:54:57 2022

@author: ni664326
"""

import os # for setting up proper working directory
import pandas as pd # for reading and viewing data
import matplotlib.pyplot as plt # for visualizing data
import seaborn as sns # another way to view data
import numpy as np # to build arrays
import scipy as sp # for descriptive statistics
import statsmodels.stats.weightstats as sm # more descriptive statistics


#3 Read in data and change header names

os.getcwd()
git_path = 'C:\\Users\\ni664326\\OneDrive - Knights - University of Central Florida\\Classes\\Summer 2022\\Business Analytics - ECO 5445\\GitHub\\ECO5445\\'
os.chdir(git_path + 'Project\\Data')

PrjData = pd.read_csv("hmda_sw.csv", header=0, names=colNames1, delimiter = ",")

colNames1 = ["SEQ", "LoanType", "LoanPurpose", "Occupancy", "LoanAmmount", "TypeAction", "MSAloc", "CountryLoc", "RaceAppl", "RaceCoApp", "SexApp", "SexCoApp", "AppIncome", "PurchaserType", "HMDAorig", "Correction1", "Correction2", "Correction3", "UnitsProp", "MaritalStatus", "DependentsApp", "YearsAppLW", "YearsAppJob", "SelfEmpApp", "BaseMontlyIncomeApp", "BaseMonthlyIncomeCoApp", "TotalMonthlyIncomeApp", "TotalMonthlyIncomeCoApp", "ProposedMonthlyHouseExp", "PurchasePrice", "OtherFinancing", "LiquidAssets", "CommercialCredit", "AppHistoryGood", "CreditLines", "CH_mortgage", "CH_consumer", "CH_public", "Debt/IncomeHousing", "Debt/IncomeTotal", "F_or_A_loan", "TermLoan", "SpecialLoanApp", "AppraisedValue", "TypeProperty", "PMIsought", "PMIdenied", "Gift/GrantDP", "CoSign", "UnverifiableInfo", "#Reviewed", "netw", "uria", "rtdum", "bd", "mi", "old", "vr", "school", "chvalc", "dnotown", "dprop"]

PrjData.to_csv("PrjData.csv")
summaryRace = PrjData.RaceAppl.describe()
print(summaryRace)

PrjData.RaceAppl
PrjData["RaceAppl"]
sp.stats.describe(PrjData["RaceAppl"])
                  
#4 Summary statistics

PrjData.TypeAction.describe()
PrjData["TypeAction"]

PrjData.TypeAction.value_counts()
PrjData.RaceAppl.value_counts()
