from flask import Flask, render_template, request
from cal import calculate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_result():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = int(request.form['operation'])

    result = calculate(num1, num2, operation)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)