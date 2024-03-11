from behave import given, when, then
# from pages.search_page import SearchPage
# from pages.cart_page import CartPage
from pages.checkout_page import Checkoutpage
from pages.login_page import Login_page
from behave.api.async_step import async_run_until_complete


@when('I add the product to my cart')
@async_run_until_complete
async def add_product_to_cart(context):
    context.search_page = Checkoutpage(context.page)
    await context.search_page.add_product_to_cart()

@when('I proceed to checkout')
@async_run_until_complete
async def proceed_to_checkout(context):
    context.search_page = Checkoutpage(context.page)
    await context.search_page.product_checkout()

@then('I should complete the checkout process successfully')
@async_run_until_complete
async def complete_checkout_success(context):
    context.search_page = Checkoutpage(context.page)
    await context.search_page.checkout_page_title('Select a delivery address')
