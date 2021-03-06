from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def hello():
    return 'goodbye'

@app.route('/')
def home():
    return render_template('Page1.html')
    
@app.route('/pieteikties')
def pieteikties():
    return render_template('pieteiktViziti.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/manasp')
def manaspieties():
    return render_template('jusuVizite.html')

@app.route('/register')
def register():
    return render_template('SecondPage.html')

@app.route('/stat')
def stat():
    return render_template('Page9.html')

@app.route('/mekletarstu')
def meklet():
    return render_template('Page4.html')

@app.route('/apraksts')
def apraksts():
    return render_template('Page6.html')

app.run(host='0.0.0.0', port=5017, debug=True)