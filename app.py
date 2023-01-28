from flask import Flask, render_template
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():  # check if running on pythonanywhere
        app.run()