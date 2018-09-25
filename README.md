# UI Testing using Selenium and Behave Framework

# General
The purpose of this repo is to present an example of UI testing using Selenium Webdriver under the Behave Framework (BDD)

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, 
QA and non-technical or business participants in a software project

For more info on Behave please look at the following link: https://behave.readthedocs.io/en/latest/

Selenium WebDriver is a collection of language specific bindings to drive a browser, more info in: https://www.seleniumhq.org/

# Prerequisites

In order to execute the test scripts you need:

- Python2 (https://www.python.org/downloads/release/python-2715/)
- Behave (https://behave.readthedocs.io/en/latest/index.html)
- Selenium (https://www.seleniumhq.org/download/)

Web browser driver, geckodriver (firefox) and chromedriver (chrome) are included in this repo

# How to execute the scripts
After cloning the repo execute the command "behave"

If more information is needed, use: "behave --no-capture --no-capture-stderr -f pl"

# Test Procedure

Constraints:
1) Use the content of the input.json file as body in the POST message
2) "hookinstance" value should be a random string for every run

The purpose of this test is to check the UI, the steps are:

1) Send a POST request to receive the url to verify
2) Parse the response and obtain the url
3) Login to the url with the usr and psw provided
4) Once logged in, click the "Next" button
5) In the next page click the "Copy accepted" button
6) Wait for browser to redirect to "about:blank"
6) Send the same POST request as 1)

# Some details about the implementation

- I use the requests module since I found it has good flexibility in handling HTTP messages
- I use the uuid module to create the random string for "hookInstance" since it will make it more unique
- I use find.element.by.id to locate the usr/psw fields and find.element.by.xpath for the buttons
- The scripts were tested in both Chrome and Firefox
- Even if is not required to check the POST response, I still verify that the body is not empty in the second case

