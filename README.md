# Playwright Search Test Suite

A small pytest suite using Playwright to automate and test search on DuckDuckGo, written while learning browser automation.

## What it tests
- A search query appears in the resulting page title (run with two different terms)
- A deliberately wrong search term correctly fails the check
- The homepage's search box is visible before any interaction

## How to run it

pip install pytest playwright
python -m playwright install
python -m pytest -v


Note: tests open a real browser via Playwright and hit the live DuckDuckGo site, so they need internet and a few seconds per run.
