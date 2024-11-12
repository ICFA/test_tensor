from pages.sbis_contacts import SbisContacts
from pages.tensor_main import TensorMain
from pages.tensor_about import TensorAbout

def test_on_sbis_contacts_page(browser):
    sbis_contacts_page = SbisContacts(browser)
    sbis_contacts_page.go_to_site()
    sbis_contacts_page.click_on_tensor()

def test_on_tensor_main_page(browser):
    tensor_main_page = TensorMain(browser)
    tensor_main_page.go_to_site()
    tensor_main_page.check_about_block()
    tensor_main_page.click_on_about()

def test_on_tensor_about_page(browser):
    tensor_about_page = TensorAbout(browser)
    tensor_about_page.go_to_site()
    widths, heights = tensor_about_page.check_photos()
    assert len(widths) == 1
    assert len(heights) == 1