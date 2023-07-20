from flask import Flask, request, jsonify, render_template
from calculator import AddOperator, SubtractOperator, DivideOperator, MultiplyOperator

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def perform_calculation():
    operator = request.form['operator']
    operand1 = float(request.form['operand1'])
    operand2 = float(request.form['operand2'])

    # Implement the business logic for calculations using the Strategy pattern
    try:
        if operator == '+':
            calculator = AddOperator()
        elif operator == '-':
            calculator = SubtractOperator()
        elif operator == '/':
            calculator = DivideOperator()
        elif operator == '*':
            calculator = MultiplyOperator()
        else:
            return jsonify({'error': 'Invalid operator'})

        result = calculator.calculate(operand1, operand2)
        return jsonify({'result': result})
    except ZeroDivisionError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
