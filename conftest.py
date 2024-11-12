import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    edge_options = webdriver.EdgeOptions()
    prefs = {"download.default_directory": r"D:\Program Files\GitHub\test_tensor"}
    edge_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
