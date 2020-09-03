import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestPythonOrgTest(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.driver

    def test_get_todo_list(self):
        # setup
        self.driver.get('https://www.python.org/')
        assert 'Python' in self.driver.title

        self.driver.find_element_by_link_text('Downloads').click()

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.download-list-widget .widget-title'))
        )
        assert 'Looking for a specific release?' == element.text

        self.driver.find_element_by_link_text('Documentation').click()

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'call-to-action'))
        )
        assert 'Browse the docs' in element.text

        element = self.driver.find_element_by_name('q')
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)

        assert 'No results found' not in self.driver.page_source
