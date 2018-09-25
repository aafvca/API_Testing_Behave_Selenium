Feature: UI Test

  Scenario: Get url from POST request
    Given Set POST api endpoint as "https://interview.evinance.net/rest/cds-services/app"
    When set HEADER param request content type as "application/json"
      And Set BODY from "input.json"
      And hookinstance value is a random String
      And Send POST HTTP Request
    Then Valid HTTP Response should be received
      And Response http code should be 200
	  And Response HEADER content type should be "application/json"
	  And Response BODY should not be null or empty
	  And Response BODY parsing for next url should be successful

  Scenario: Browser interaction
    Given The username is "qa@example.com"
      And The psw is "DJcS2Mk83u"
    When Login in url from POST message
      And Click the Next button
      And Click the Copy Accepted button
    Then The POST request from previous scenario is sent
      And Response http code should be 200
	  And Response HEADER content type should be "application/json"
	  And Response BODY should not be null or empty
