from flask import Flask, render_template, request
import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get')
# def get():    
#     querystring = request.args
#     return render_template('data.html', data = querystring, method = 'get')

@app.route('/post', methods = ['POST'])
def post():
    # Get the parsed contents of the form data
    form = request.form
    fname = request.form.getlist('fname')
    print fname
    return render_template('data.html', data = form, method = 'post')

if __name__ == '__main__':
    app.run(debug= True)
    

