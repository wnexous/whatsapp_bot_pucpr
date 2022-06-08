from playwright.sync_api import Playwright, sync_playwright, expect

import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://web.whatsapp.com/
    page.goto("https://web.whatsapp.com/")
    time.sleep(10)
    # Click text=oii1
    #page.locator("text=oii1").click()
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # Click ._2nY6U.vq6sj._2_TVt ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn
    #page.locator("._2nY6U.vq6sj._2_TVt ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn").click()
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # Click ._2nY6U.vq6sj._2_TVt ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn
    #page.locator("._2nY6U.vq6sj._2_TVt ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn").click()
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # Click text=+55 41 9826-434309:35+55 41 9826-4344: 11
    #page.locator("text=+55 41 9826-434309:35+55 41 9826-4344: 11").click()
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # Click text=+55 41 9826-434409:332
    #page.locator("text=+55 41 9826-434409:332").click()
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # Click ._2nY6U.vq6sj._2_TVt ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn
    print('a')
    while True:
        try:
            receb = page.query_selector("._2nY6U.vq6sj._3C4Vf ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn")
            texto = receb.text_content()
            print(texto)
            if "24" in texto:
                break
            receb.click()
            page.keyboard.insert_text(texto)
            page.keyboard.press('Enter')
            page.locator("text=[HUB] Nexous").click()
        except Exception:   pass
        
    # expect(page).to_have_url("https://web.whatsapp.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
