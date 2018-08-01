from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# for maintainability of waits during execution


class WaitFor(object):

    @staticmethod
    def element(driver, *value):
        element = driver.find_element(*value)
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(element))
        return element
