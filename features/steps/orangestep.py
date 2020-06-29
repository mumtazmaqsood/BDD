from behave import *
from selenium import webdriver

@given('launch chrome browser')
def open_browser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\Drivers\chm\chromedriver.exe")
    context.driver=webdriver.Chrome()
@when('open organg hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify logo present on the home page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close browser')
def close_browser(context):
    context.driver.close()