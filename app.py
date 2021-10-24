from os import link
from flask import Flask, request, render_template, redirect, url_for
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 83b8fd649927745cad5907cad74f3617cf8bf970
    link = str(main.createPlaylist(playName, playLen))
    return redirect(url_for("link_share"))

@app.route('/results')
def link_share():
    global link
    webbrowser.open_new_tab(link)
    return redirect(url_for("searchify"))
=======
    return main.createPlaylist(playName, playLen)
    # return redirect(url_for("searchify"))

# @app.route('/results')
# def link_share():
#     return render_template('')
>>>>>>> 700c6fa90cbe509bf46619506fbd80d63288defb

if __name__ == "__main__":
    app.run()