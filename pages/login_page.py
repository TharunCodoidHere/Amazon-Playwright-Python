from pages.base_page import BasePage
from playwright.async_api import Page
import time
import sys
# from playwright.sync_api import Locator
class Login_page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open(self):
        await self.page.goto("https://www.amazon.in/", timeout=60000)
        # title = await self.page.title()
        # print(title)
        time.sleep(2)

    async def click_signin(self):
        try:
            time.sleep(2)
            await self.page.click("#nav-link-accountList-nav-line-1")  #
        # await self.page.wait_for_selector('//span[text()="Sign in"]', timeout=5000)
        # await self.page.click('//span[text()="Sign in"]')
        except Exception as e:
            print(f"Error occurred: {str(e)}")

    async def login(self, username, password):
        try:
            await self.page.fill("//*[@id='ap_email']", username)  # Replace "#username" with the actual selector for the username input field
            await self.page.click('#continue')
            await self.page.fill("#ap_password", password)  # Replace "#password" with the actual selector for the password input field
            await self.page.click("#signInSubmit")  # Replace "button#login-submit" with the actual selector for the login submit button
        except Exception as e:
            print(f"Error occurred: {str(e)}")

    async def is_user_logged_in(self,prof_name):
                profile_name=await self.page.text_content(f'//span[text()="{prof_name}"]')
                print('______profile_name______',profile_name)
                # text = await profile_name.textContent()
                assert prof_name== profile_name
                print('__________',profile_name)
        
    async def home_page_title(self,page_title):
        time.sleep(3)
        title = await self.page.title()
        assert title==page_title
        print(title)
        time.sleep(2)

    async def verify_sigin_page(self):
         time.sleep(5)
         sigin_page=await self.page.query_selector("//div[@class='a-box-inner a-padding-extra-large']//h1")
         print('___________________SiginPage Verification___________________',sigin_page)
         await sigin_page.is_visible()
        