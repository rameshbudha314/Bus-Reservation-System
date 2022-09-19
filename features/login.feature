Feature: Login
    As a user,
    I want to able to login my account,
    so that I can book bus seat

Scenario: Login
    Given users visit the login page
    Then users provide registered username and password
    Then the response status should be 200