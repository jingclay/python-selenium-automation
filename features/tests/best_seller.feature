Feature: Amazon best seller tests

  Scenario: BestSellers page has 5 links
    Given Open amazon page
    Then click best sellers
    Then Verify that best seller has 5 links