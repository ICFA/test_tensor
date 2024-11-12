from pages.sbis_contacts import SbisContacts

def test_on_sbis_contacts_page(browser):
    sbis_contacts_page = SbisContacts(browser)
    sbis_contacts_page.go_to_site()
    assert sbis_contacts_page.check_region().text == "Свердловская обл."
    sbis_contacts_page.check_partners()
    assert sbis_contacts_page.change_region_to_41() == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    assert sbis_contacts_page.check_title() == "СБИС Контакты — Камчатский край"
    assert sbis_contacts_page.check_region().text == "Камчатский край"
    assert sbis_contacts_page.check_partners_changed().text == "Петропавловск-Камчатский"
