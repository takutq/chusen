from flask import render_template, request, redirect, url_for
from chusentest import app
from random import randint

from chusentest import db
from chusentest.models.guest import Guest

@app.route('/')
def index():
    return render_template('chusen/index.html')

@app.route('/test')
def other1():
    return render_template('chusen/index2.html')

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET': #GETの時/sampleform.html表示
        return render_template('chusen/sampleform.html')
    if request.method == 'POST':    #POSTの時data1をreturn
        print('post受け取り完了')
        req1 = request.form['data1']
        return f'POST受け取った: {req1}'

@app.route('/add_guest', methods=['GET', 'POST'])
def add_guest():
    if request.method == 'GET':
        return render_template('chusen/add_guest.html')
    if request.method == 'POST':
        guest = Guest(
            ic_card = '2222222',
            name = 'namae',
            age = '18',
        )
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for('index'))
