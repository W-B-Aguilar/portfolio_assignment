from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def project():
    return render_template('project.html')

@app.route('/about')
def aboutme():
    return render_template('about.html')

app.run(debug=True)