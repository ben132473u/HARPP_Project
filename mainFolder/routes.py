from mainFolder import app
#, mysql, bcrypt, phone
from flask import render_template, flash, redirect, url_for, request
from mainFolder import dao
#, session, logging, request, g, make_response
#from flask_mysqldb import MySQL
#from passlib.hash import sha256_crypt
#import json
#import pandas as pd
#from datetime import datetime, timedelta,timezone
#from time import strftime
#from pytz import timezone
#import tzlocal
#import uuid
#import os
#import xlsxwriter
#from openpyxl import load_workbook
#import subprocess
#import cookies
#from bs4 import BeautifulSoup
#import requests
#import urllib.request
#import mechanize
#import http.cookiejar as cookielib

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')
    
@app.route("/mainPage", methods=['GET', 'POST'])
def mainPage():
    # for all the template pages, render this.
    return render_template('mainpage.html', title='Home')

@app.route("/viewListing", methods=['GET', 'POST'])
def viewListing():
    if request.method == 'POST':
        requestedID = request.form.get('requestID')
        print(requestedID)
        file = open('test.txt', 'w+')
        file.write(requestedID)
        file.close()
        return redirect('predictionTool')
    if request.method == 'GET':
        requestedID = dao.daoTest()
        file = open('test.txt', 'w+')
        file.write(str(requestedID))
        file.close()
        return redirect('predictionTool')
    return render_template('viewlisting.html', title='View Listing')

@app.route("/predictionTool", methods=['GET', 'POST'])
def predictionTool():
    return render_template('predictiontool.html', title='Prediction Tool')

@app.route("/viewAnalytics", methods=['GET', 'POST'])
def viewAnalytics():
    return render_template('viewanalytics.html', title='View Analytics')

@app.route("/test1", methods=['GET', 'POST'])
def test1():
    #if request.methods="POST":
    return render_template('test.html', title='Home')



##then when u need to have dynamic functions on page i.e clicking a button, saving some data
# use ajax instead. then call the function itself

@app.route("/function", methods=['GET', 'POST'])
def function():
    #get your data from your html
    return render_template('test.html', title='Home')
