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
    result = app.test_client().get('/froyo_results?flavor=chocoloate&toppings=syrup')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered chocolate flavored Fro-Yo with toppings syrup!'
    assert expected_page_text == result_page_text
    

def test_froyo_results_strawberry():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific scenario.
    result = app.test_client().get('/froyo_results?flavor=strawberry&toppings=sprinkles!')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered chocolate flavored Fro-Yo with toppings sprinkles'
    assert expected_page_text == result_page_text

def test_froyo_results_edgecase1():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific EDGE CASE scenario.
    pass

def test_froyo_results_edgecase2():
    # TODO: Fill in this function to test the show_froyo_results route under a
    # specific EDGE CASE scenario.
    pass


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

def test_message_results_scenario2():
    # TODO: Fill in this function to test the message_results route under 
    # another scenario.
    pass

def test_message_results_edgecase1():
    # TODO: Fill in this function to test the message_results route under 
    # an edge case scenario.
    pass


#######################
# Calculator Tests
#######################

def test_calculator_results_scenario1():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    pass

def test_calculator_results_scenario2():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    pass

def test_calculator_results_scenario3():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    pass

def test_calculator_results_scenario4():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific scenario.
    pass

def test_calculator_results_edgecase1():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific EDGE CASE scenario.
    pass

def test_calculator_results_edgecase2():
    # TODO: Fill in this function to test the calculator_results route under a
    # specific EDGE CASE scenario.
    pass