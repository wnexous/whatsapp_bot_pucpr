from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://pt.wikipedia.org/wiki/Feij%C3%A3o_carioca")
    a= page.locator('text=feijão').text_content()
    print(a)
    
    
    