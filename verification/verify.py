from playwright.sync_api import sync_playwright
import os

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Base URL (assuming default port 3000 from npm run dev, which usually runs browser-sync or similar)
        # Checking package.json to confirm start command...
        # 'dev' runs 'npm-run-all --parallel tailwind:watch serve'
        # 'serve' runs 'browser-sync start --server --files ...'
        # BrowserSync usually defaults to 3000.
        base_url = "http://localhost:3000"

        os.makedirs("verification", exist_ok=True)

        # Verify grid.html
        print("Verifying grid.html...")
        page.goto(f"{base_url}/grid.html")
        page.wait_for_load_state("networkidle")
        # Check for the header icon change
        page.screenshot(path="verification/grid.png")

        # Verify html-basics.html
        print("Verifying html-basics.html...")
        page.goto(f"{base_url}/html-basics.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/html-basics.png")

        # Verify api.html
        print("Verifying api.html...")
        page.goto(f"{base_url}/api.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/api.png")

        # Verify ejercicio-api.html
        print("Verifying ejercicio-api.html...")
        page.goto(f"{base_url}/ejercicio-api.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/ejercicio-api.png")

        # Verify ejercicio-responsive.html
        print("Verifying ejercicio-responsive.html...")
        page.goto(f"{base_url}/ejercicio-responsive.html")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="verification/ejercicio-responsive.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
