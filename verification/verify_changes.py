from playwright.sync_api import sync_playwright
import os

def verify(page):
    # Verify index.html
    page.goto("http://localhost:3000/index.html")
    page.screenshot(path="verification/index.png", full_page=True)
    print("Screenshot of index.html saved.")

    # Verify ejercicio-grid.html
    page.goto("http://localhost:3000/ejercicio-grid.html")
    page.screenshot(path="verification/ejercicio-grid.png", full_page=True)
    print("Screenshot of ejercicio-grid.html saved.")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    verify(page)
    browser.close()
