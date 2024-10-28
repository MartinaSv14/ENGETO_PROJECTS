#Test to check whether the Page title on https://engeto.cz/absolventi/ matches.

import re
from playwright.sync_api import expect

def test_check_page_title(page):    
    page.goto("https://engeto.cz/")
    print("Waiting for Info about Cookies")

    print("Waiting for Cookies pop up")
    button = page.get_by_role("button", name="Chápu a přijímám!", exact=True)
    button.click()

    print("Click on Reference a příběhy")
    button = page.get_by_text("Reference a příběhy", exact=True)
    #button = page.get_by_text("Průvodce IT", exact=True) #---> If active, while making inactive row 13, test should failed.
    button.click()

    if page.title == ("Reference a příběhy absolventů | ENGETO"):
        print (f"Page title is correct")
    else:
        print (f"Page title is incorrect")

    print(f"Page title: {page.title()}, while expected: Reference a příběhy absolventů | ENGETO")
    expect(page).to_have_title("Reference a příběhy absolventů | ENGETO")
    





    



# Assert the page title
   # pageTitle = page.Title
    #if (pageTitle -eq "Reference a příběhy absolventů | ENGETO")
    #print("Page title is correct")
    #else {
    #print("Page title is incorrect")


    #button = page.get_by_role("button", name="Souhlasím s vybranými", exact=True)
   # button.click()

