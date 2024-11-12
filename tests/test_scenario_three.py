from pages.sbis_main import SbisMain
from pages.sbis_download import SbisDownload

def test_on_sbis_main_page(browser):
    sbis_main_page = SbisMain(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_on_download_local_versions()

def test_on_sbis_download_page(browser):
    sbis_download_page = SbisDownload(browser)
    sbis_download_page.go_to_site()
    sbis_download_page.click_on_download_web()
    assert sbis_download_page.check_dowloaded_file()
    assert sbis_download_page.check_dowloaded_file_checksum() == "2ec6dba8863795e477ae80b395ac0153"