from mainFolder import app
#, mysql, bcrypt, phone
from flask import render_template, flash, redirect, url_for
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
@app.route("/mainPage", methods=['GET', 'POST'])
def mainPage():
    # for all the template pages, render like this.
    return render_template('mainpage.html', title='Home')

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
