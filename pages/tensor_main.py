from Base import BasePage
from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_ABOUT_BLOCK = (By.CLASS_NAME, "tensor_ru-Index__block4-content.tensor_ru-Index__card")
    LOCATOR_ABOUT_BUTTON = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

class TensorMain(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, base_url="https://tensor.ru")

    def check_about_block(self):
        return self.find_element(Locators.LOCATOR_ABOUT_BLOCK)

    def click_on_about(self):
        about_button = self.find_element(Locators.LOCATOR_ABOUT_BUTTON)
        self.base_url = about_button.get_attribute('href')
        return self.go_to_site()
