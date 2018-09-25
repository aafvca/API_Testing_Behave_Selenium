from behave import given, when, then
import requests, json, uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


global_general_variables = {}
http_request_header = {}
http_request_body = {}

@given(u'Set POST api endpoint as "{post_api_endpoint}"')
def step_impl(context, post_api_endpoint):
    global_general_variables['POST_api_endpoint'] = post_api_endpoint

@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type

@when(u'Set Body from "{post_body_file}"')
def step_impl(context, post_body_file):
    with open(post_body_file) as f:
        http_request_body['body'] = json.load(f)

@when(u'hookinstance value is a random String')
def step_impl(context):
    hookInstanceValue = str(uuid.uuid4())
    http_request_body['body']['hookInstance'] = hookInstanceValue

@when(u'Send POST HTTP Request')
def step_impl(context):
    url_temp = global_general_variables['POST_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers = http_request_header,
                                                              data = json.dumps(http_request_body['body']))

@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'

@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Response BODY parsing for next url should be successful')
def step_impl(context):
    full_message = global_general_variables['response_full'].json()
    url_link = full_message['cards'][0]['links'][0]['url']
    global_general_variables['url_link'] = url_link

@given(u'The username is "{user_name}"')
def step_impl(context, user_name):
    global_general_variables['user_name'] = user_name

@given(u'The psw is "{user_psw}"')
def step_impl(context,user_psw):
    global_general_variables['user_psw'] = user_psw

@when(u'Login in url from POST message')
def step_impl(context):
    url = global_general_variables['url_link']
    usr = global_general_variables['user_name']
    psw = global_general_variables['user_psw']
    context.browser.get(url)
    context.browser.find_element_by_id("username").clear()
    context.browser.find_element_by_id("username").send_keys(usr)
    context.browser.find_element_by_id("password").clear()
    context.browser.find_element_by_id("password").send_keys(psw)
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    WebDriverWait(context.browser, 60).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='recommendations-next']" )))

@when(u'Click the Next button')
def step_impl(context):
    context.browser.find_element_by_xpath("//button[@id='recommendations-next']").click()
    WebDriverWait(context.browser, 60).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='summary-copy-accepted']" )))


@when(u'Click the Copy Accepted button')
def step_impl(context):
    context.browser.find_element_by_xpath("//button[@id='summary-copy-accepted']").click()
    WebDriverWait(context.browser, 60).until(EC.title_contains, "about:blank")

@then(u'The POST request from previous scenario is sent')
def step_impl(context):
    url_temp = global_general_variables['POST_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers = http_request_header,
                                                              data = json.dumps(http_request_body['body']))
