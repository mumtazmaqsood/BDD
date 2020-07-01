from behave import *
from selenium import webdriver

@given('Lanuch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('Open orangHRM homepage')
def open_browser(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def login_info(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when('Click on Login Button')
def login_btn(context):
    context.driver.find_element_by_xpath("//input[@id='btnLogin']").click()


@then(u'user must successfully login to Dashboard page')
def main_page(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]")
    assert text == "Dashboard"
    context.driver.close()