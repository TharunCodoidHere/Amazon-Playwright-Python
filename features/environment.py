from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright


@fixture
async def browser_chrome(context):
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, args=['--incognito'])
    context.page = await browser.new_page()
    return context.page


@async_run_until_complete
async def before_feature(context, scenario):
    await use_fixture(browser_chrome, context)