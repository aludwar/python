from flask import Flask, request, render_template, url_for, flash, redirect

app = Flask(__name__)

def get_enmax_floats(f1,f2,f3,f4,f5):
    while True:
        try:
            n1 = float(f1)
            n2 = float(f2)
            n3 = float(f3)
            n4 = float(f4)
            n5 = float(f5)
        except ValueError:
            print("Input should be numbers. Try again.")
        else:
            return n1, n2, n3, n4, n5

def get_cui_floats(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    while True:
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
        else:
            return n1, n2, n3, n4, n5, n6, n7, n8, n9

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    provider = request.form['target']
    EnmaxField1 = request.form['Enmax.eusage']
    EnmaxField2 = request.form['Enmax.ngusage']
    EnmaxField3 = request.form['Enmax.ecost']
    EnmaxField4 = request.form['Enmax.ngcost']
    EnmaxField5 = request.form['Enmax.tcost']
    fields = (EnmaxField1 + EnmaxField2 + EnmaxField3)
    return(str(provider))


