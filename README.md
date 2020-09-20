# BDD (Behaviour Driven Development) Project
using python behave package

    Feature: Check Login Credentials
      Scenario: Login to orangeHRM with valid parameters
        Given Lanuch Chrome Browser
        When Open orangHRM homepage
        And Enter username "Admin" and password "admin123"
        And Click on Login Button
        Then user must successfully login to Dashboard page
  
    
    Feature: OrangeHRM Logo
      Scenario: Logo presense on OrangeHRM  home page
        Given launch chrome browser
        When open organg hrm homepage
        Then verify logo present on the home page
        And close browser