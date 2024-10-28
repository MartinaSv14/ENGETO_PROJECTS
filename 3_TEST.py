#Test to check whether there is at least 1 course available on https://engeto.cz/terminy/.

def test_count_date_filters(page):
    page.set_default_timeout(100000)
    print("Navigating to Engeto")
    page.goto("https://engeto.cz/")
    
    print("Waiting for Info about Cookies")
    button = page.get_by_role("button", name="Chápu a přijímám!", exact=True)
    button.click()

    print("Click on button Zobrazit termíny kurzů")
    button = page.get_by_role("link", name="Zobrazit termíny kurzů")
    button.click()

    date_filters = page.locator(".dates-filter-column > .block-button:visible")
    page.wait_for_selector(".dates-filter-column > .block-button:visible", timeout=1000000)
    
    count = date_filters.count()
    print(f"Results: {count}")
    assert count > 0
