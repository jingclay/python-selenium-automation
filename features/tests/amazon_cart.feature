
Feature: Empty Cart

  Scenario: Verifies that Your Amazon Cart is empty
    Given Open Amazon page
    When Click Cart icon from popup
    Then Verify Your Amazon Cart is Empty


