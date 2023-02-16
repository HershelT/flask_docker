from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='Templates')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/sum')
def sum():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return str(num1 + num2)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)