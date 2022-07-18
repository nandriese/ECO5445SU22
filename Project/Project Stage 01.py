# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:54:57 2022

@author: ni664326
"""

from tabulate import tabulate
import os  # for setting up proper working directory
import pandas as pd  # for reading and viewing data
import matplotlib.pyplot as plt  # for visualizing data
import seaborn as sns  # another way to view data
import numpy as np  # to build arrays
import scipy as sp  # for descriptive statistics
import statsmodels.stats.weightstats as sm  # more descriptive statistics


# 3 Read in data and change header names

os.getcwd()
git_path = 'C:\\Users\\ni664326\\OneDrive - Knights - University of Central Florida\\Classes\\Summer 2022\\Business Analytics - ECO 5445\\GitHub\\ECO5445\\'
os.chdir(git_path + 'Project\\Data')

PrjData = pd.read_csv("hmda_sw.csv", header=0, names=colNames1, delimiter=",")

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


# 4 Summary statistics
sp.stats.describe(PrjData[["TypeAction","RaceAppl", "Debt/IncomeHousing", "Debt/IncomeTotal", "SelfEmpApp", "school", "AppIncome", "LoanType", "LoanPurpose", "Occupancy", "LoanAmmount", "old", "netw", "PMIsought", "PMIdenied", "YearsAppLW", "YearsAppJob", "TotalMonthlyIncomeApp", "TotalMonthlyIncomeCoApp", "ProposedMonthlyHouseExp", "PurchasePrice", "TermLoan", "AppraisedValue", "TypeProperty", "OtherFinancing", "LiquidAssets", "CommercialCredit", "AppHistoryGood", "CreditLines", "CH_mortgage", "CH_consumer", "CH_public"]])
PrjData.MaritalStatus.value_counts()
r = np.corrcoef(myvariables)
print(r)
sp.stats.describe(myvariables)

PrjData.plot
plt.hist(PrjData["RaceAppl"])
plt.hist(PrjData["Debt/IncomeTotal"])
plt.scatter(PrjData["Debt/IncomeTotal"], PrjData["PurchasePrice"])
# 5 Baseline Probability of being approved for a mortgage

PrjData.TypeAction.value_counts()
Approve = 2025+70
Denied = 285
TotalApplicants = Approve + Denied
ProbApprove = Approve/TotalApplicants
print(ProbApprove)
# 88% Approval rate

# Tried the below but couldn't get it to work:
Approve = 0
Denied = 0

if PrjData.TypeAction == 1 | 2:
    Approve += 1
Denied += 1
############################

# 6 Table

pip install tabulate


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

table = [["Applicant Race", "Approved", "Not Approved", "Total"], ["Black", BlackApp, BlackDeny,
                                                                   BlackTot], ["White", WhiteApp, WhiteDeny, WhiteTot], ["Total", TotApp, TotDeny, AllTotal]]
print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# 7
ProbAppWhite = WhiteApp/WhiteTot
print(ProbAppWhite)
ProbNotAppBlack = BlackDeny/BlackTot
print(ProbNotAppBlack)
