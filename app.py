from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Set the path to the templates folder
app.config['TEMPLATE_FOLDER'] = os.path.join(os.getcwd(), 'templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error! Division by zero.'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
