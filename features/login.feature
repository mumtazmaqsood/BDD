Feature: Check Login Credentials
  Scenario: Login to orangeHRM with valid parameters
    Given Lanuch Chrome Browser
    When Open orangHRM homepage
    And Enter username "admin" and password "admin123"
    And Click on Login Button
    Then user must successfully login to Dashboard page
