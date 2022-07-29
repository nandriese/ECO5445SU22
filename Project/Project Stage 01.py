# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:54:57 2022

@author: ni664326
"""
###############################################################################
# Copy header formatting from my scripts
###############################################################################

from tabulate import tabulate
import os  # for setting up proper working directory
import pandas as pd  # for reading and viewing data
import matplotlib.pyplot as plt  # for visualizing data
#import seaborn as sns  # another way to view data
import numpy as np  # to build arrays
import scipy as sp  # for descriptive statistics
#import statsmodels.stats.weightstats as sm  # more descriptive statistics

###############################################################################
# Included packages that weren't needed
###############################################################################

###############################################################################
# Also, be sure not to add things such as pip install within the python file
# This will cause your file not to fully run and you'll have errors
###############################################################################

# 3 Read in data and change header names

os.getcwd()
git_path = 'C:\\Users\\ni664326\\OneDrive - Knights - University of Central Florida\\Classes\\Summer 2022\\Business Analytics - ECO 5445\\GitHub\\ECO5445\\'
git_path = 'C:/Users/jo585802/OneDrive - University of Central Florida/Documents/GitHub/ECO5445/' # Needed line to test data
os.chdir(git_path + 'Project/Data')


colNames1 = ["SEQ", "LoanType", "LoanPurpose", "Occupancy",
             "LoanAmmount", "TypeAction", "MSAloc", "CountryLoc", "RaceAppl",
             "RaceCoApp", "SexApp", "SexCoApp", "AppIncome", "PurchaserType",
             "HMDAorig", "Correction1", "Correction2", "Correction3", "UnitsProp",
             "MaritalStatus", "DependentsApp", "YearsAppLW", "YearsAppJob", "SelfEmpApp",
             "BaseMontlyIncomeApp", "BaseMonthlyIncomeCoApp", "TotalMonthlyIncomeApp",
             "TotalMonthlyIncomeCoApp", "ProposedMonthlyHouseExp", "PurchasePrice",
             "OtherFinancing", "LiquidAssets", "CommercialCredit", "AppHistoryGood",
             "CreditLines", "CH_mortgage", "CH_consumer", "CH_public", "Debt/IncomeHousing",
             "Debt/IncomeTotal", "F_or_A_loan", "TermLoan", "SpecialLoanApp", "AppraisedValue",
             "TypeProperty", "PMIsought", "PMIdenied", "Gift/GrantDP", "CoSign",
             "UnverifiableInfo", "#Reviewed", "netw", "uria", "rtdum", "bd", "mi",
             "old", "vr", "school", "chvalc", "dnotown", "dprop"]

###############################################################################
# Colnames must go before reading in file
###############################################################################

PrjData = pd.read_csv("hmda_sw.csv", header=0, names=colNames1, delimiter=",") 

###############################################################################
# The categorical variables are currently being treated as numeric. You cannot
# do mean, sd, etc.
###############################################################################

PrjData.to_csv("PrjData.csv")
summaryRace = PrjData.RaceAppl.describe()
print(summaryRace)

PrjData.RaceAppl
PrjData["RaceAppl"]
sp.stats.describe(PrjData["RaceAppl"])
#DV: "TypeAction"
# covariates:
# Required: "Debt/IncomeHousing", "Debt/IncomeTotal", "RaceAppl", "MaritalStatus", "SelfEmpApp", "school
# Others: "AppIncome", "LoanAmmount", "old", "netw", "PMIsought", "PMIdenied",
# Others: "YearsAppLW", "YearsAppJob","TotalMonthlyIncomeApp",
# Others: "TotalMonthlyIncomeCoApp", "ProposedMonthlyHouseExp", "PurchasePrice", "TermLoan", "AppraisedValue","TypeProperty"
# Others: "LiquidAssets", "CommercialCredit", "AppHistoryGood", "CreditLines", "CH_mortgage", "CH_consumer", "CH_public"
myvariables = PrjData["TypeAction"], PrjData["RaceAppl"], PrjData["Debt/IncomeHousing"], PrjData["Debt/IncomeTotal"], PrjData["RaceAppl"], PrjData["SelfEmpApp"], PrjData["school"], PrjData["AppIncome"], PrjData["LoanPurpose"], PrjData["Occupancy"], PrjData["LoanAmmount"], PrjData["old"], PrjData["netw"], PrjData["PMIsought"], PrjData["PMIdenied"], PrjData["YearsAppLW"], PrjData["YearsAppJob"], PrjData[
    "TotalMonthlyIncomeApp"], PrjData["TotalMonthlyIncomeCoApp"], PrjData["ProposedMonthlyHouseExp"], PrjData["PurchasePrice"], PrjData["TermLoan"], PrjData["AppraisedValue"], PrjData["TypeProperty"], PrjData["OtherFinancing"], PrjData["LiquidAssets"], PrjData["CommercialCredit"], PrjData["AppHistoryGood"], PrjData["CreditLines"], PrjData["CH_mortgage"], PrjData["CH_consumer"], PrjData["CH_public"]
# marital status needs to be recoded as integers, ran out of time PrjData["MaritalStatus"]

###############################################################################
# Why did you choose these variables in particular? What information from the
# paper helped you decide?
###############################################################################

###############################################################################
# Didn't happen to notice that 999,999.4 is the designation for missing 
# numerical data. Summary statistics will be skewed.
###############################################################################

# 4 Summary statistics
sp.stats.describe(PrjData[["TypeAction","RaceAppl", "Debt/IncomeHousing", "Debt/IncomeTotal", "SelfEmpApp", "school", "AppIncome", "LoanType", "LoanPurpose", "Occupancy", "LoanAmmount", "old", "netw", "PMIsought", "PMIdenied", "YearsAppLW", "YearsAppJob", "TotalMonthlyIncomeApp", "TotalMonthlyIncomeCoApp", "ProposedMonthlyHouseExp", "PurchasePrice", "TermLoan", "AppraisedValue", "TypeProperty", "OtherFinancing", "LiquidAssets", "CommercialCredit", "AppHistoryGood", "CreditLines", "CH_mortgage", "CH_consumer", "CH_public"]])

PrjData.MaritalStatus.value_counts()

###############################################################################
# This is what you needed to do as well for other qualitative variables. 
# Race isn't a number, it is a category.
###############################################################################

PrjData.RaceAppl.value_counts()

###############################################################################
# Brought in qualitative in with quantatitive varaibles. This correlation
# is hard to read without labels on them.
###############################################################################

r = np.corrcoef(myvariables)
print(r)


sp.stats.describe(myvariables)


PrjData.plot

plt.hist(PrjData["RaceAppl"])
###############################################################################
# Histograms are not used for categorical data. Additionally, this chart would
# be hard to understand if you do not know what 2 or 4 means.
###############################################################################

###############################################################################
# These plots do not provide details about what we are plotting
# They need context in order to understand.
###############################################################################
plt.hist(PrjData["Debt/IncomeTotal"])
plt.scatter(PrjData["Debt/IncomeTotal"], PrjData["PurchasePrice"])
PrjData[["RaceAppl", "TypeAction"]].groupby("RaceAppl").value_counts()
PrjData[["RaceAppl", "SelfEmpApp"]].groupby("RaceAppl").value_counts()

###############################################################################
# What does all this mean for the representative applicant?
# What does it mean about the sample?
###############################################################################

# 5 Baseline Probability of being approved for a mortgage

PrjData.TypeAction.value_counts()

###############################################################################
# This next part requires you to look at a table, then manually input values.
# We can extract values from the tables instead of hand typing them
###############################################################################

Approve = 2025+70
Denied = 285
TotalApplicants = Approve + Denied
ProbApprove = Approve/TotalApplicants
print(ProbApprove)
# 88% Approval rate


############################

# 6 Table



PrjData[["RaceAppl", "TypeAction"]].groupby("RaceAppl").value_counts()
BlackApp = 233 + 10
BlackDeny = 96
BlackTot = BlackApp + BlackDeny
WhiteApp = 1792 + 60
WhiteDeny = 189
WhiteTot = WhiteApp + WhiteDeny
TotApp = BlackApp + WhiteApp
TotDeny = BlackDeny + WhiteDeny
AllTotal = TotApp + TotDeny

# not sure if there is a way to extract the value counts and save them into a variable rather than doing it manually

###############################################################################
# There is a way we can get around this by extracting values from tables
###############################################################################

table = [["Applicant Race", "Approved", "Not Approved", "Total"], ["Black", BlackApp, BlackDeny,
                                                                   BlackTot], ["White", WhiteApp, WhiteDeny, WhiteTot], ["Total", TotApp, TotDeny, AllTotal]]
print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# 7
ProbAppWhite = WhiteApp/WhiteTot
print(ProbAppWhite)
ProbNotAppBlack = BlackDeny/BlackTot
print(ProbNotAppBlack)
