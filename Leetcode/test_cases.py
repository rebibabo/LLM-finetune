from playwright.sync_api import Playwright, sync_playwright
import pyperclip
import os

def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://leetcode.cn/")
    page.locator("#navbar_sign_in_button").click()
    page.locator("#qr-code-flag").click()
    page.wait_for_selector("#navbar_user_avatar", timeout=60000)

    return browser, context, page

change_language = True
def test(brower, context, page, code, url: str) -> None:
    global change_language
    page.goto(url)
    if change_language:
        change_language = False
        page.wait_for_selector("#editor [aria-expanded=false]")
        page.locator("#editor [aria-expanded=false]").click()
        lcs = page.locator(".text-text-primary.text-sm").all()
        for lc in lcs:
            if lc.inner_text() == 'Python3':
                lc.click()
                break
    pyperclip.copy(code)
    lc = page.locator("#editor .view-lines")
    lc.click()
    lc.press("Control+a")
    lc.press("Control+v")

    page.get_by_role("button", name="提交").click()
    page.wait_for_selector("#submission-detail_tab")
    
    while page.locator("#submission-detail_tab div.medium.whitespace-nowrap.font-medium").inner_text() == 'Loading...':
        pass    

    if page.locator("#submission-detail_tab div.medium.whitespace-nowrap.font-medium").inner_text() == "通过":
        return True
    return False

start_index = 52
start = False
with open('Leetcode/urls.txt', 'r') as f:
    lines = f.readlines()

test_results = []
with sync_playwright() as playwright:
    browser, context, page = login(playwright)
    for i, file in enumerate(os.listdir('dataset/leetcode')):
        num = int(file.split('.')[0])
        if num != start_index and not start:
            continue
        start = True
        url = lines[num-1].split(' ')[1]
        with open(f'dataset/leetcode/{file}', 'r') as f:
            code = f.read()
        correct = test(browser, context, page, code, url)
        test_results.append((num, correct))
        print(num, correct)
    context.close()
    browser.close()

with open('Leetcode/results.txt', 'w') as f:
    for num, correct in test_results:
        f.write(f'{num} {correct}\n')
