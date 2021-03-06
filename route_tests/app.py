from flask import Flask, request

from unit_tests.string_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/color_form')
def show_color_form():
    return """
    <form action="/color_results" method="GET">
        <label>
            What's your favorite color?
            <input type="text" name="color">
        </label>
        <input type="submit" name="Submit!">
    </form>
    """

@app.route('/color_results')
def process_color_results():
    users_favorite_color = request.args.get('color')
    if users_favorite_color != '':
        return f"Wow, {users_favorite_color} is my favorite color, too!"
    else:
        return "You didnt specify a color!"


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/><br/>
        What toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    toppings = request.args.get('toppings')
    if users_froyo_flavor != '':
        return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {toppings}!'
    else:
        return "Please input your favorite flavor and topping."


@app.route('/reverse_message')
def reverse_message_form():
    return """
    <form action="/message_results" method="POST">
        What's your message?
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    message = request.form.get('message')
    reversed_message = reverse(message)
    if message == '':
        return "Please enter a message."
    else:
        return f'Here\'s your reversed message: {reversed_message}'


@app.route('/calculator', methods=['POST'])
def calculator():
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/calculator_results', methods=['POST'])
def calculator_results():

    operation = request.form.get('operation')

    try:
        operand1 = int(request.form.get('operand1'))
        operand2 = int(request.form.get('operand2'))
    except ValueError:
        return "Please enter a valid number"

    if operation == '':
        return "Please enter a valid operation"


    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    else:
        result = operand1 / operand2

    return f'You chose to {operation} {operand1} and {operand2}. Your result is: {result}'


if __name__ == '__main__':
    app.run(debug=True)