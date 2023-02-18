
Feature: Returns and Orders

  Scenario: Amazon users see Returns & Orders  button
    Given Open Amazon page
    When Click Returns & Orders from popup
    Then Verify Sign In header is visible
    Then Verify email input field is present

