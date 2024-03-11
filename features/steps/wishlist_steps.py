from behave import given, when, then
# from pages.search_page import SearchPage
# from pages.cart_page import CartPage
from pages.checkout_page import Checkoutpage
from pages.search_page import Searchpage
from pages.wishlist_page import Wishlistpage
from behave.api.async_step import async_run_until_complete

@when('I click on my wishlist link')
@async_run_until_complete
async def  i_click_on_my_wish(context):
    context.whish_page = Wishlistpage(context.page)
    context.whish_page.wishlist_page()

@then('I should see My Wishlist Page')
@async_run_until_complete
async def  i_see_my_wishlist_page(context):
    context.whish_page.shoppinglist_page()