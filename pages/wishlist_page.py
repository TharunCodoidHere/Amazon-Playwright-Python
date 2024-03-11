import time
from pages.base_page import BasePage
from playwright.async_api import Page

class Wishlistpage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def wishlist_page(self):
        element_to_hover = await self.page.query_selector("#nav-link-accountList-nav-line-1")
        await element_to_hover.hover()
        await self.page.wait_for_timeout(500)

        element_to_click = await self.page.query_selector("//div[@id='nav-al-your-account']//span[text()='Your Wish List']")
        await element_to_click.click()

    async def shoppinglist_page(self):
        shoplist_element=await self.page.query_selector('//span[text()="Shopping List" and @id="profile-list-name"]')
        await shoplist_element.is_visible()
