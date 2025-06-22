import asyncio
from playwright.async_api import async_playwright
from markdownify import markdownify as md

async def get_chapter_markdown(url, screenshot_path="chapter1_screenshot.png", html_path="chapter1.html", md_path="chapter1.md"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path=screenshot_path, full_page=True)
        content_html = await page.inner_html("#mw-content-text")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content_html)
        md_text = md(content_html)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        await browser.close()
        return md_text