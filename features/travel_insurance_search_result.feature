@travel_insurance @search_result
Feature: Verify the search functionality of Travel Insurance section
  As a user I want to perform a quick search to looking for information about Travel Insurance

  @id-1 @top3_card_brand_names
  Scenario Outline: Verify that at least 3 Provider Result should be displayed after click on Show Result button
    Given the user is standing at home page
    When the user clicks on Insurance tab
    And the user clicks on Travel tab
    And the user clicks on Show my Results button
    Then the user should see 3 card brands "<brand name list>" are displaying in the top 3 of Result Grid

  Examples:
    | brand name list |
    | Malayan Insurance, Malayan Insurance, Standard Insurance |


  @id-2 @filter_overview_values
  Scenario: Verify that the filter overview in Travel Insurance Search Result page displays corrects information of users selected options
    Given the user is standing at home page
    When the user clicks on Insurance tab
    And the user clicks on Travel tab
    And the user selected below options in Travel Insurance Search box
      | field       | value       |
      | Policy Type | single trip |
      | Whos Going  | just me     |
      | Destination | Thailand    |
      | Start Date  | 10-06-2019  |
      | End Date    | 15-06-2019  |
    And the user clicks on Show my Results button
    Then the user should see the filter overview in Tralvel Insurance Search Result page is displaying users selected options correctly