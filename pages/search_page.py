import time
from pages.base_page import BasePage
from playwright.async_api import Page

class Searchpage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def search_field(self,product):
        await self.page.fill("#twotabsearchtextbox", product)
        await self.page.click('#nav-search-submit-button') 
        time.sleep(10)
        print('searched_product',await self.page.title())

    async def search_page_title(self,page_title):
        # page_tit= BasePage.is_title_contains('Amazon.in : redmi 9 prime')
        page_tit= await self.page.title()
        assert page_title== page_tit
