import time
from pages.base_page import BasePage
from playwright.async_api import Page

class Checkoutpage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # async def search_field(self,product):
    #     await self.page.fill("#twotabsearchtextbox", product)
    #     await self.page.click('#nav-search-submit-button') 
    #     time.sleep(10)
    #     print('searched_product',await self.page.title())
        # await search_input.is_visible()

    async def  add_product_to_cart(self):
        print("___add_product____")
        time.sleep(10)
        # await self.page.goto("https://www.amazon.in/Renewed-Redmi-Storage-Display-Camera/dp/B08PKTMZPR/ref=sr_1_1?crid=3PFAK1YNA6NBF&dib=eyJ2IjoiMSJ9.a07Lnr20SztPRIzDs0DG-sXw_54IVY6p2FPZqC2vIOSgZ0MxoNKqZtqYeaYXM9Kq_cRzgsPfL2rJhmIJXvEM1ogYS9m_BaGNyY-SmoQgZONHQDP2-Nn24maDy8YKZmNWirh6XYLBldHgZYxqYAtvEfFQficPfVknCT_uU-je4qJ4FxUXPA2jsaG8ptPZoHvfyDxHlqsykHAnVF_Orem9aI6fshjazHZg-F1NqZdqvr4.AGDMPfrV-Hry-pS0EYzs9vNP3T4IAKnXJDPQfa5jWhw&dib_tag=se&keywords=redmi+9+prime&qid=1709665571&sprefix=redmi+9+prime%2Caps%2C401&sr=8-1", timeout=10000)
        await self.page.click('((//div[@id="s-skipLinkTargetForMainSearchResults"]//following::h2)//parent::div//parent::div//parent::div//parent::div//preceding-sibling::div)[1]')
        time.sleep(7)
        print('_____clicked_____')
        time.sleep(25)
        # await self.page.wait_for_new_window()
        new_window = await self.page.wait_for_event('popup', timeout=35000)
    
    # Switch context to the new window
        await new_window.bring_to_front()
        print(new_window)
        print('_____Switched_____')
        print('_____TITLE______',await new_window.title())
        time.sleep(6)
        await new_window.click('//input[@id="add-to-cart-button"]')
        print('____Added______')
        # await self.page.contexts()[1].bring_to_front()

    # Switch to the new window
        # await self.page.bring_to_front()
        # await self.page.contexts()[1].bring_to_front()
        # await self.page.click('(//div[@id="addToCart_feature_div"])[2]')

        # async def verify_sigin_page(self):
        time.sleep(5)
        added_to_cart=await new_window.query_selector("//div[@id='attach-added-to-cart-alert-and-image-area']//h4[text()='Added to Cart']")
        print('___________________SiginPage Verification___________________',added_to_cart)
        await added_to_cart.is_visible()
        print('____________Verified____________')
        await new_window.click("//span[@id='attach-sidesheet-checkout-button']")

    async def product_checkout(self):
        checkout_page=await self.new_window.query_selector('//div[@class="a-column a-span8"]//h1')
        await checkout_page.is_visible()

    async def checkout_page_title(self,title):
        await BasePage.is_title_contains(title)

