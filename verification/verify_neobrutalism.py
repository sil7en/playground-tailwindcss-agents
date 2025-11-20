
from playwright.sync_api import sync_playwright
import os

def verify_neobrutalism():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        index_path = f"file://{cwd}/index.html"

        print(f"Navigating to {index_path}")
        page.goto(index_path)

        # Take screenshot of the homepage
        screenshot_path = f"{cwd}/verification/homepage_neobrutalism.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_neobrutalism()
