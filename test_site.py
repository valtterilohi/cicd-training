import pytest
import os
from playwright.sync_api import sync_playwright

def test_heading():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Tämä hakee index.html-tiedoston polun tästä samasta kansiosta
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = f"file://{os.path.join(current_dir, 'index.html')}"
        
        page.goto(file_path)
        
        # Tarkistetaan otsikko
        heading = page.inner_text("h1")
        assert heading == "CI/CD Training"
        
        browser.close()