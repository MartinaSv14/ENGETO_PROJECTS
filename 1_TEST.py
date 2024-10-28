#Test to check whether there is at least 1 reference/story visible on page https://engeto.cz/absolventi/ (using filter Současná pozice).
   
def test_absolvents_stories(page):
    print("Navigating to Engeto")
    page.goto("https://engeto.cz/")
    
    print("Waiting for Info about Cookies")

    print("Waiting for Cookies pop up")
    button = page.get_by_role("button", name="Chápu a přijímám!", exact=True)
    button.click()

    print("Click on Stories")
    button = page.get_by_role("link", name="Reference a příběhy")
    button.click()

    #Programování filter
    print("Click on Stories Programování")
    button = page.get_by_text("Programování", exact=True)
    button.click()

    print("Stories_Prog check")
    stories_prog = page.locator(".zf-tg-graduate:visible")
    count = stories_prog.count()
    print(f"results Prog: ({count})")
    assert count > 0

    #Datová analýza filter
    print("Click on Stories Datová analýza")
    button = page.get_by_text("Datová analýza")
    button.click()

    print("Stories_Dat_Ana check")
    stories_dat_ana = page.locator(".zf-tg-graduate:visible")
    count1 = stories_dat_ana.count()
    print(f"results Dat_ana: ({count1})")
    assert count1 > 0

    #Testování filter
    print("Click on Stories Testování")
    button = page.get_by_text("Testování")
    button.click()

    print("Stories_Test check")
    stories_test = page.locator(".zf-tg-graduate:visible")
    count2 = stories_test.count()
    print(f"results Test: ({count2})")
    assert count2 > 0

    #Systémová administrace filter
    print("Click on Stories Systémová Administrace")
    button = page.get_by_text("Systémová administrace")
    button.click()

    print("Stories_Syst_Adm check")
    stories_syst_adm = page.locator(".zf-tg-graduate:visible")
    count3 = stories_syst_adm.count()
    print(f"results Syst_Adm: ({count3})")
    assert count3 > 0
    
    #IT konzultace filter
    print("Click on Stories IT konzultace")
    button = page.get_by_text("IT konzultace")
    button.click()

    print("Stories_Konz check")
    stories_konz = page.locator(".zf-tg-graduate:visible")
    count4 = stories_konz.count()
    print(f"results Konz: ({count4})")
    assert count4 > 0