
#this is so powerful py script testing for linter
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

#testing for linter(error)
if nnc:
    gotohell


@app.route('/health')
def health():
    return 'Server is up and running'
