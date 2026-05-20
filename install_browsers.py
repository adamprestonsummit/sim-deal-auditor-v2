# On Railway, Playwright Chromium is installed at build time via railway.toml
# This file is kept as a safe no-op for compatibility
import os

def install_playwright_browsers():
    """No-op on Railway — browser is installed at build time."""
    pass

install_playwright_browsers()
