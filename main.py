#!/usr/bin/python
# -*- coding: UTF-8 -*-


import asyncio
from playwright.async_api import async_playwright
from settings import (
    URL,
    DRIVER_PATH,
    CHROME_PATH,
    ACC,
    PWD,
    BuyerSSN,
    BirthYear,
    BirthMonth,
    BirthDay,
    multi_CVV2Num,
)

selectors = {
    "add_to_cart": "#ButtonContainer > button",
    "loging_acc": "#loginAcc",
    "loging_pw": "#loginPwd",
    "loging_click": "#btnLogin",
}


async def login(page):
    await page.click(selectors["loging_acc"])
    await page.fill(selectors["loging_acc"],ACC)
    await page.click(selectors["loging_pw"])
    await page.fill(selectors["loging_pw"],PWD)
    await asyncio.sleep(5)
    await page.click(selectors["loging_click"])

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        try:
            context = await browser.new_context(storage_state="state.json")
        except FileNotFoundError:
            context = await browser.new_context()
        page = await context.new_page()
        await page.goto(URL)
        await page.click(selectors["add_to_cart"])
        await page.goto(
            "https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList"
        )
        page_url = page.url
        if page_url.find("login") != -1:
            await login(page)
            await context.storage_state(path="state.json")
        # print(await page.title())
        # await browser.close()
        await asyncio.sleep(5)


asyncio.run(main())
