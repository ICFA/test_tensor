from Base import BasePage
from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_PHOTOS = (By.CLASS_NAME, "tensor_ru-About__block3-image")

class TensorAbout(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver, base_url="https://tensor.ru/about")

    def check_photos(self):
        photos = self.find_elements(Locators.LOCATOR_PHOTOS)
        width_set = set()
        height_set = set()
        for photo in photos:
            width_set.add(photo.get_attribute('width'))
            height_set.add(photo.get_attribute('height'))
        return (width_set, height_set)
