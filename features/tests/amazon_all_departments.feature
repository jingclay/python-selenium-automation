Feature: Amazon main page tests


  Scenario: User can use All Departments dropdown and search for an item
   Given open Amazon page
   When hover over the "All Departments" dropdown menu
   When Select department Amazon Fresh
   When input text food ready to eat
   When Click on search button
   Then Verify search results are displayed