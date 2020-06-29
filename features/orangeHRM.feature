Feature: OrangeHRM Logo
  Scenario: Logo presense on OrangeHRM  home page
    Given launch chrome browser
    When open organg hrm homepage
    Then verify logo present on the home page
    And close browser