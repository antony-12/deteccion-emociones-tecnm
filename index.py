#index.pyy
from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL
import sys
import numpy

# initializations ss
app = Flask(__name__)


# settings
app.secret_key = "mysecretkey"


# Main
@app.route('/')
def Index():
    
    return render_template('index.html')

# Main
@app.route('/original')
def original():
    
    return render_template('original.html')

# Main
@app.route('/cargando')
def cargando():
    
    return render_template('cargando.html')

@app.route('/carga2')
def carga2():
    
    return render_template('carga2.html')

@app.route('/inner')
def inner():
    
    return render_template('inner.html')


# starting the app
if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)