from os import link
from flask import Flask, request, render_template, redirect, url_for
from components import WebBrowser
import webbrowser
import main
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
link = ""
run = False

@app.route('/')
def searchify():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def searchify_results():
    global link
    playName = request.form['playName']
    playLen = request.form['playLen']
    link = str(main.createPlaylist(playName, playLen))
    WebBrowser.printLink(link)
    return redirect(url_for("link_share"))

@app.route('/results')
def link_share():
    global link
    webbrowser.open_new_tab(link)
    #return render_template('index copy.html', data=link)
    return redirect(url_for("searchify"))

if __name__ == "__main__":
    app.run()