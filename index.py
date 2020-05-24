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
@app.route('/document')
def documentt():
    
    return render_template('document.html')



# starting the app
if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)