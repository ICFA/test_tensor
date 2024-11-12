from Base import BasePage
from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_DOWNLOAD_LOCAL_VERSIONS = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')

class SbisMain(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver, base_url="https://sbis.ru")

    def click_on_download_local_versions(self):
        self.find_element(Locators.LOCATOR_DOWNLOAD_LOCAL_VERSIONS).click()
        return
