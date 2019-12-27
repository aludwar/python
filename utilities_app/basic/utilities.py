#!/usr/bin/python3

import subprocess, datetime, time
from datetime import timedelta
from decimal import *
from influxdb import InfluxDBClient
from flask import Flask, request, render_template, url_for, flash, redirect

host = '<hostname>'
port = '8086'
user = 'admin'
password = '<password>'
dbname = 'utilities_new'

app = Flask(__name__)

def subtract_one_month(dt0):
    dt1 = dt0.replace(day=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(day=1)
    return dt3

def get_enmax_floats(f1,f2,f3,f4,f5):
  try:
    getcontext().prec = 2
    n1 = float(f1)
    n2 = float(f2)
    n3 = float(f3)
    n4 = float(f4)
    n5 = float(f5)
  except ValueError:
    print("Input should be numbers. Try again.")
    return 500
  else:
    return n1, n2, n3, n4, n5

def get_cui_floats(f1,f2,f3,f4,f5,f6,f7,f8,f9):
  try:
    n1 = float(f1)
    n2 = float(f2)
    n3 = float(f3)
    n4 = float(f4)
    n5 = float(f5)
    n6 = float(f6)
    n7 = float(f7)
    n8 = float(f8)
    n9 = float(f9)
  except ValueError:
    print("Input should be numbers. Try again.")
    return 500
  else:
    return n1, n2, n3, n4, n5, n6, n7, n8, n9

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    provider = str(request.form['target'])

    if provider == 'Enmax':
      EnmaxEusage = request.form['Enmax.eusage']
      EnmaxNGusage = request.form['Enmax.ngusage']
      EnmaxEcost= request.form['Enmax.ecost']
      EnmaxNGcost = request.form['Enmax.ngcost']
      EnmaxTcost = request.form['Enmax.tcost']
      EnmaxYear = str(subtract_one_month(datetime.datetime.now()))
      EnmaxYear = int(EnmaxYear[0:4])

      try:
        EnmaxMonth = int(request.form['emonth'])
      except ValueError:
        print("Please select a month")
        return 'Please select a month'

      dt = datetime.datetime(year=EnmaxYear, month=EnmaxMonth, day=15)
      EnmaxEpoch = time.mktime(dt.timetuple())
      utilities_tuple = get_enmax_floats(EnmaxEusage, EnmaxNGusage, EnmaxEcost, EnmaxNGcost, EnmaxTcost)
      if utilities_tuple == 500:
        return 'Input should be numbers. Try again.'
      else:
        dbclient = InfluxDBClient(host, port, user, password, dbname)
        
        json_body = [
        {
            "measurement": "utilities",
            "tags": {
                "vendor": "enmax"
            },
            "time": EnmaxEpoch,
            "fields": {
                "electricity_usage": (utilities_tuple[0]),
                "natural_gas_usage": (utilities_tuple[1]),
                "electrical_cost": (utilities_tuple[2]),
                "natural_gas_cost": (utilities_tuple[3]),
                "carbon_levy": Decimal(0),
                "total_cost": (utilities_tuple[4]),
            }
        }
        ]
        
        dbclient.write_points(json_body)

        return 'OK'

    elif provider == 'CUI':
      CUIgarbage = request.form['CUI.garbage']
      CUIrecycle = request.form['CUI.recycle']
      CUIrstorm = request.form['CUI.rstorm']
      CUIrsewer = request.form['CUI.rsewer']
      CUIrwater = request.form['CUI.rwater']
      CUIwusage = request.form['CUI.wusage']
      CUIwcost = request.form['CUI.wcost']
      CUIscost = request.form['CUI.scost']
      CUItcost = request.form['CUI.tcost']
      CUIEpoch = int(time.time()) 
      utilities_tuple = get_cui_floats(CUIgarbage, CUIrecycle, CUIrstorm, CUIrsewer, CUIrwater, CUIwusage, CUIwcost, CUIscost, CUItcost)
      if utilities_tuple == 500:
        return 'Input should be numbers. Try again.'
      else:
        utilities_list = list(utilities_tuple)
        utilities_list.append(CUIEpoch)
        print(utilities_list)
        return 'OK'


