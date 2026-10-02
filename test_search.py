import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def test_duckduckgo_search_shows_results(page):
        page.goto("https://duckduckgo.com")
        page.fill("textarea[name='q']", "Playwright Python")
        page.press("textarea[name='q']", "Enter")
        page.wait_for_timeout(5000)
        assert "Playwright Python" in page.title()

def test_duckduckgo_search_shows_results_second_run(page):
        page.goto("https://duckduckgo.com")
        page.fill("textarea[name='q']", "LoRaWAN Guide 457炒面")
        page.press("textarea[name='q']", "Enter")
        page.wait_for_timeout(5000)
        assert "LoRaWAN Guide 457炒面" in page.title()

#fail option
def test_duckduckgo_search_shows_banana(page):
        page.goto("https://duckduckgo.com")
        page.fill("textarea[name='q']", "Playwright Python")
        page.press("textarea[name='q']", "Enter")
        page.wait_for_timeout(5000)
        assert "banana" in page.title()

def test_duckduckgo_homepage_has_search_box(page):
    page.goto("https://duckduckgo.com")
    assert page.is_visible("textarea[name='q']")