from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    #context.browser = webdriver.Firefox(executable_path="geckodriver.exe")
    context.browser = webdriver.Chrome(executable_path="chromedriver.exe")
    #Linux
    #context.browser = webdriver.Chrome("/full/path/to/chromedriver")

def after_all(context):
    context.browser.quit()
