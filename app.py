from flask import Flask, request, render_template
import main
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')  

@app.route('/')
def searchify():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def searchify_results():
    playName = request.form['playName']
    playLen = request.form['playLen']
    return main.createPlaylist(playName, playLen)

if __name__ == "__main__":
    app.run()