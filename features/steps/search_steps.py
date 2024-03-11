from behave import given, when, then
# from pages.search_page import SearchPage
# from pages.cart_page import CartPage
from pages.checkout_page import Checkoutpage
from pages.search_page import Searchpage
from pages.login_page import Login_page
from behave.api.async_step import async_run_until_complete

@given('I am on the homepage')
@async_run_until_complete
async def am_on_the_homepage(context):
    context.loginPage = Login_page(context.page)
    await context.loginPage.is_user_logged_in('Hello, Tharun')

@when('I search for a product')
@async_run_until_complete
async def search_for_product(context):
    context.search_page = Searchpage(context.page)
    await context.search_page.search_field("redmi 9 prime")

@then('I should see the page title relevant to search result')
@async_run_until_complete
async  def check_title(context):
    await context.search_page.search_page_title('Amazon.in : redmi 9 prime')