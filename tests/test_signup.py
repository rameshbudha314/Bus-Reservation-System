"""login feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import requests

@scenario('../features/login.feature', 'login')
def test_login():
    """login."""


@given('users visit the login page', target_fixture='response')
def user_visits_user_dashboard_or_navigation_bar():
    response = requests.get('http://localhost:8000/signout')
    return response


@then('the response status should be 200')
def the_response_status_should_be_200(response):
    """the response status should be 200."""
    assert 200 == response.status_code


@then('user press login button')
def user_press_login_button(response):
    """user press login button."""
    assert 'Sign in' in response.text

