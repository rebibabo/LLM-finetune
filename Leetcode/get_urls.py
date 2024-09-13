from playwright.sync_api import Playwright, sync_playwright
from tqdm import trange

def run(playwright: Playwright) -> None:
    with open('urls.txt', 'w') as f:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        cnt = 1
        for page_index in trange(1, 73):
            page.goto(f"https://leetcode.cn/problemset/?page={page_index}")
            page.wait_for_timeout(5000)
            lcs = page.locator(".truncate .h-5")
            for problem_index in range(50):     # 第一页的题目索引要加一
                problem_page = f'https://leetcode.cn{lcs.nth(problem_index + int(page_index == 1)).get_attribute("href")}/description'
                f.write(str(cnt) + ' ' + problem_page + '\n')
                cnt += 1
                f.flush()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    # 获取系统参数
    run(playwright)

