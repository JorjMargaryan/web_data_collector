from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage


class ResourcesArea(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the ResourcesArea class.
        """
        super().__init__(driver)
        self.__contactsButtonLocator = (By.CSS_SELECTOR, "#navitem_about_contacts")

    def click_to_contacts_button(self):
        """
            Clicks the Contacts button in the Resources area.
        """
        contactsButtonElement = self._find_element(self.__contactsButtonLocator)
        self._click_to_element(contactsButtonElement)
