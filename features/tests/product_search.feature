# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Dress into search field
    And Click on search icon
    Then Product results for Dress are shown

Scenario: Add product on Amazon can be shown in the cart
    Given Open Amazon page
    When Input text stone maidens book
    When Click on search button
    When Click on stone maidens by Richards
    When Click Add to Cart button
    Then Click Cart icon from popup
    Then Verify that stone maidens is present in the cart