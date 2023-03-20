# Created by svetlanalevinsohn at 2/25/23
Feature: Amazon Sign in tests



Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page opens


Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present


Scenario: 'Add a product to cart'
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present

