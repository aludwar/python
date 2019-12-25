from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    EnmaxField1 = request.form['Enmax.field1']
    EnmaxField2 = request.form['Enmax.field2']
    EnmaxField3 = request.form['Enmax.field3']
    fields = (EnmaxField1 + EnmaxField2 + EnmaxField3)
    return fields


