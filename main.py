#-----------------------------------------
# main.py: handles project webpage requests
#-----------------------------------------
from flask import Flask, render_template
import json

app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/statistics')
def statistics():
	return render_template('statistics.html')

if __name__ == "__main__":
    app.run()
#----------------------------------------
# end of main.py
#-----------------------------------------
