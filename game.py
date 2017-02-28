from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = random.randrange(0,101)
        # print session['answer']
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # print "getting guess " + request.form['guess']
    # print "session answer is " + str(session['answer'])

    return render_template('index.html', guess = int(request.form['guess']), answer = session['answer'])

@app.route('/reset')
def reset():
    session.pop('answer')
    return redirect('/')

app.run(debug=True)
