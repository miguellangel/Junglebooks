#-----------------------------------------
# main2.py: creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/book/')
def web_page2():
    return render_template('web_page2.html')
if __name__ == "__main__":
    app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------
