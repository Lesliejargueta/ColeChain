from flask import Flask, render_template
from data import ColeBases

app= Flask(__name__)

ColeBases = ColeBases()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/colebases')
def colebases():
    return render_template('colebases.html', colebases=ColeBases)

@app.route('/colebase/<int:Data>/')
def colebase(Data):
    return render_template('colebase_detail.html', colebase=ColeBases[Data-1])

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/jobsnru')
def jobsnru():
    return render_template('jobsnru.html')

if __name__== '__main__':
    app.run(debug=True)
