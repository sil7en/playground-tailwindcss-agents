
from playwright.sync_api import sync_playwright
import os

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the index.html file
        current_dir = os.getcwd()

        # Verify index.html
        page.goto(f"file://{current_dir}/index.html")
        page.screenshot(path="verification/index_screenshot.png", full_page=True)

        # Verify html-basics.html
        page.goto(f"file://{current_dir}/html-basics.html")
        page.screenshot(path="verification/html_basics_screenshot.png", full_page=True)

        # Verify css-basics.html
        page.goto(f"file://{current_dir}/css-basics.html")
        page.screenshot(path="verification/css_basics_screenshot.png", full_page=True)

        # Verify tailwind-basics.html
        page.goto(f"file://{current_dir}/tailwind-basics.html")
        page.screenshot(path="verification/tailwind_basics_screenshot.png", full_page=True)

        # Verify responsive.html
        page.goto(f"file://{current_dir}/responsive.html")
        page.screenshot(path="verification/responsive_screenshot.png", full_page=True)

        # Verify flex.html
        page.goto(f"file://{current_dir}/flex.html")
        page.screenshot(path="verification/flex_screenshot.png", full_page=True)

        # Verify grid.html
        page.goto(f"file://{current_dir}/grid.html")
        page.screenshot(path="verification/grid_screenshot.png", full_page=True)

        # Verify ejercicio-flex.html
        page.goto(f"file://{current_dir}/ejercicio-flex.html")
        page.screenshot(path="verification/ejercicio_flex_screenshot.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_frontend()
