import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################

def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################

def test_color_results_blue():
    result = app.test_client().get('/color_results?color=blue')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, blue is my favorite color, too!'
    assert expected_page_text == result_page_text

def test_color_results_light_green():
    # TODO: Fill in this function to test the color_results route under 
    # a specific scenario.
    result = app.test_client().get('/color_results?color=light%20green')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, light green is my favorite color, too!'
    assert expected_page_text == result_page_text


def test_color_results_empty():
    # TODO: Fill in this function to test the color_results route under 
    # an edge case scenario.
    result = app.test_client().get('/color_results?color=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You didnt specify a color!'
    assert expected_page_text == result_page_text



#######################
# Froyo Tests
#######################

def test_froyo_results_chocolate():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific scenario.
    result = app.test_client().get('/froyo_results?flavor=chocolate&toppings=syrup')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered chocolate flavored Fro-Yo with toppings syrup!'
    assert expected_page_text == result_page_text
    

def test_froyo_results_strawberry():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific scenario.
    result = app.test_client().get('/froyo_results?flavor=strawberry&toppings=sprinkles')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered strawberry flavored Fro-Yo with toppings sprinkles!'
    assert expected_page_text == result_page_text

def test_froyo_results_empty_flavor():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific EDGE CASE scenario.
    result = app.test_client().get('/froyo_results?flavor=&toppings=sprinkles')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Please input your favorite flavor and topping.'
    assert expected_page_text == result_page_text

def test_froyo_results_empty_both():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific EDGE CASE scenario.
    result = app.test_client().get('/froyo_results?flavor=&toppings=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Please input your favorite flavor and topping.'
    assert expected_page_text == result_page_text

#######################
# Reverse Message Tests
#######################

def test_message_results_helloworld():
    form_data = {
        'message': 'Hello World'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'dlroW olleH' in result_page_text

def test_message_results_welcomealex():
    # TODO: Fill in this function to test the message_results route under 
    # another scenario.
    form_data = {
        'message': 'Welcome Alex'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'xelA emocleW' in result_page_text

def test_message_results_blank():
    # TODO: Fill in this function to test the message_results route under 
    # an edge case scenario.
    form_data = {
        'message': ''
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'Please enter a message.' in result_page_text


#######################
# Calculator Tests
#######################

def test_calculator_results_add():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    form_data = {
        'operand1': '2',
        'operand2': '2',
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You chose to add 2 and 2. Your result is: 4' in result_page_text

def test_calculator_results_subtract():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    form_data = {
        'operand1': '20',
        'operand2': '10',
        'operation': 'subtract'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You chose to subtract 20 and 10. Your result is: 10' in result_page_text

def test_calculator_results_multiply():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    form_data = {
        'operand1': '5',
        'operand2': '20',
        'operation': 'multiply'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You chose to multiply 5 and 20. Your result is: 100' in result_page_text

def test_calculator_results_divide():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    form_data = {
        'operand1': '75',
        'operand2': '5',
        'operation': 'divide'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You chose to divide 75 and 5. Your result is: 15' in result_page_text

def test_calculator_results_operands():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific EDGE CASE scenario.
    pass
#    form_data = {
#        'operand1': None,
#        'operand2': '2',
#        'operation': 'add'
#    }
#    res = app.test_client().post('/calculator_results', data=form_data)
#    assert res.status_code == 200

#    result_page_text = res.get_data(as_text=True)
#    assert 'Please check to see if you input everything.' in result_page_text

def test_calculator_results_operation():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific EDGE CASE scenario.
    pass
#    form_data = {
#        'operand1': '2',
#        'operand2': '2',
#        'operation': None
#    }
#    res = app.test_client().post('/calculator_results', data=form_data)
#    assert res.status_code == 200

#    result_page_text = res.get_data(as_text=True)
#    assert 'Please check to see if you input everything.' in result_page_text