from Base import BasePage
from selenium.webdriver.common.by import By
import time

class Locators:
    LOCATOR_TENSOR_BUTTON = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor.mb-12")
    LOCATOR_CURRENT_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text.sbis_ru-link")
    LOCATOR_PARTNERS_CONTAINER = (By.NAME, "itemsContainer")
    LOCATOR_41_REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    LOCATOR_41_REGION_PARTNERS = (By.ID, "city-id-2")

class SbisContacts(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, base_url="https://sbis.ru/contacts")

    def click_on_tensor(self):
        tensor_button = self.find_element(Locators.LOCATOR_TENSOR_BUTTON)
        self.base_url = tensor_button.get_attribute('href')
        return self.go_to_site()
    
    def check_region(self):
        return self.find_element(Locators.LOCATOR_CURRENT_REGION)
    
    def check_partners(self):
        return self.find_element(Locators.LOCATOR_PARTNERS_CONTAINER)
    
    def change_region_to_41(self):
        self.find_element(Locators.LOCATOR_CURRENT_REGION).click()
        self.find_element(Locators.LOCATOR_41_REGION).click()
        time.sleep(1)
        return self.driver.current_url

    def check_partners_changed(self):
        return self.find_element(Locators.LOCATOR_41_REGION_PARTNERS)
