Feature: Signup

    As a user,
    I want to able to create my acccount,
    so that I can book my bus ticket

Scenario: Signup

    Given user visits Signup page
    Then user provides details
    Then the response status should be 200
