from flask import Flask, request, render_template
import main
app = Flask(__name__)

@app.route('/')
def searchify():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def searchify_results():
    text = request.form['text']
    return main.callback(text)