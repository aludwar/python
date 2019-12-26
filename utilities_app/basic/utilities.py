from flask import Flask, request, render_template, url_for, flash, redirect
import time, sys

app = Flask(__name__)

def get_enmax_floats(f1,f2,f3,f4,f5):
  try:
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
      EnmaxEpoch = int(time.time())
      utilities = get_enmax_floats(EnmaxEusage, EnmaxNGusage, EnmaxEcost, EnmaxNGcost, EnmaxTcost)
      if utilities == 500:
        return 'Input should be numbers. Try again.'
      else:
        utilities_list = list(utilities)
        utilities_list.append(EnmaxEpoch)
        print(utilities_list)
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
      utilities = get_cui_floats(CUIgarbage, CUIrecycle, CUIrstorm, CUIrsewer, CUIrwater, CUIwusage, CUIwcost, CUIscost, CUItcost)
      if utilities == 500:
        return 'Input should be numbers. Try again.'
      else:
        utilities_list = list(utilities)
        utilities_list.append(CUIEpoch)
        print(utilities_list)
        return 'OK'


