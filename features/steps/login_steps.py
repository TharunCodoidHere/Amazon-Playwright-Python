import time
from playwright.sync_api import sync_playwright
from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from behave import given, when, then
# from pages.home_page import HomePage
from pages.login_page import Login_page


@given('I am on the Amazon homepage')
@async_run_until_complete
async def open_amazon_homepage(context):
    context.loginPage = Login_page(context.page)
    await context.loginPage.open()

@then('the  page title should contain "{title}"')
@async_run_until_complete
async def verify_homepage(context,title):
    await context.loginPage.home_page_title(title)

@when('I navigate to the login page')
@async_run_until_complete
async def navigate_to_login_page(context):
    await context.loginPage.click_signin()

@then('I should see the SignIn page')
@async_run_until_complete
async def sigin_page(context):
    await context.loginPage.verify_sigin_page()

@when('I enter valid credentials')
@async_run_until_complete
async def enter_valid_credentials(context):
    # context.loginPage = Login_page(context.page)
    await context.loginPage.login("8610366869", "Tharun@2000")

@then('I should be logged in successfully')
@async_run_until_complete
async def verify_login_success(context):
    await context.loginPage.is_user_logged_in('Hello, Tharun')