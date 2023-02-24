
Feature: Amazon add product to cart



  Scenario: Add product on Amazon can be shown in the cart
    Given Open Amazon page
    When Input text stone maidens book
    When Click on search button
    When Click on stone maidens by Richards
    When Click Add to Cart button
    Then Click Cart icon from popup
    Then Verify that stone maidens is present in the cart