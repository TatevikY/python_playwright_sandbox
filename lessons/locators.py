import re
from playwright.sync_api import Page, expect

# page.get_by_role() to locate by explicit and implicit accessibility attributes.
def test_get_by_role(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_text() to locate by text content.
def test_get_by_text(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_label() to locate a form control by associated label's text.
def test_get_by_label(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_placeholder() to locate an input by placeholder.
def test_get_by_placeholder(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_get_by_alt_text(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_title() to locate an element by its title attribute.
def test_get_by_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).
def test_get_by_test_id(page: Page):
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()