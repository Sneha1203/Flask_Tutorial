from flask import render_template

def index(name, marks):
    marks = 70
    return render_template('index.html', name=name, marks=marks)

def index_for():
    data = {
        'statitics': 70,
        'ml': 50,
        'dl': 75,
        'python': 60
    }
    return render_template('index_for.html', data=data)

