from openpyxl import load_workbook
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import sys


wb = load_workbook(filename = 'dummyData.xlsx')
sheet_ranges = wb['Sheet1'] #use sheetname as table name
#print(sheet_ranges['D4'].value)

def daoTest():
    return (sheet_ranges['D4'].value)

#ws = wb.active
#first_column = ws['B']

# Print the contents
#for x in range(len(first_column)): 
#    print(first_column[x].value) 


#data = pd.read_excel('dummyData.xlsx', index_col=None, header=0)

#print(data['open'])