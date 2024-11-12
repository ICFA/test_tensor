from Base import BasePage
from selenium.webdriver.common.by import By
import time, os, hashlib

class Locators:
    LOCATOR_DOWNLOAD_WEB = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe 11.48 МБ)')

class SbisDownload(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver, base_url="https://sbis.ru/download")

    def click_on_download_web(self):
        download_web_button = self.find_element(Locators.LOCATOR_DOWNLOAD_WEB)
        self.base_url = download_web_button.get_attribute('href')
        self.go_to_site()
        time.sleep(10)
        return
    
    def check_dowloaded_file(self):
        return os.path.exists(r"D:\Program Files\GitHub\test_tensor\sbisplugin-setup-web.exe")
    
    def check_dowloaded_file_checksum(self):
        hash_md5 = hashlib.md5()
        with open(r"D:\Program Files\GitHub\test_tensor\sbisplugin-setup-web.exe", "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()