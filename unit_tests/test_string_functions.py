import pytest

from .string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = 'gfedcba'
    actual = reverse('abcdefg')
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = 'cba'
    actual = reverse('abc')
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = 'citemhtirA'
    actual = reverse_words('Arithmetic')
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = 'olleH'
    actual = reverse_words('Hello')
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'YoU gO tO tHe GrOcErY'
    actual = sarcastic('You go to the grocery')
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'YoU dO iT'
    actual = sarcastic('You do it')
    assert actual == expected

def test_find_longest_word():
    expected = ''
    actual = ''
    assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()