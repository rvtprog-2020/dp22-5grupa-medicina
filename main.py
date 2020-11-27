from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('Page1.html')
    
@app.route('/pieteikties')
def pieteikties():
    return render_template('pieteiktViziti.html')

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

app.run(host='0.0.0.0', port=80, debug=True)