Feature: Amazon Website Functionality

  Scenario: Validate Login
    Given I am on the Amazon homepage
    Then the  page title should contain "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    When I navigate to the login page
    Then I should see the SignIn page
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Validate Search Result
    Given I am on the homepage
    When I search for a product
    Then I should see the page title relevant to search result

  Scenario: Product Checkout
    When I add the product to my cart
    When I proceed to checkout
    Then I should complete the checkout process successfully

  Scenario: Validate Product Wishlist functionality
    Given I am on the Amazon homepage
    When I click on my wishlist link
    Then I should see My Wishlist Page

  