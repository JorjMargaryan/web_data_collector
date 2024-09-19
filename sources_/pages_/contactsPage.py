from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage


class ContactsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the ContactsPage class.
        """
        super().__init__(driver)
        self.__contactsPageTitle = (By.CLASS_NAME, "h1mid")
        self.__officesDataCellLocator = (By.CSS_SELECTOR, "[itemscope='']")
        self.__countryNamesLocator = (By.CSS_SELECTOR, "[itemprop='addressLocality']")
        self.__companyNamesLocator = (By.CSS_SELECTOR, ".companydata > span:nth-child(2)")
        self.__fullAddressesLocator = (By.CSS_SELECTOR, ".companydata > span:nth-child(n+3)")

    def is_contacts_page_opened(self):
        """
            Checks if the contacts page is opened by verifying the URL and specific elements on the page.
        """
        if "contacts" in self.driver.current_url and self._is_element_visible(self.__contactsPageTitle):
            return True
        else:
            return False

    def get_country_name(self, officeDataCell):
        """
            Gets the company country name from the page.
        """
        countryNameElement = self._find_sub_element(officeDataCell, self.__countryNamesLocator)
        countryNameText = self._get_element_text(countryNameElement)
        return countryNameText

    def get_company_name(self, officeDataCell):
        """
            Gets the company name from the page.
        """
        companyNameElement = self._find_sub_element(officeDataCell, self.__companyNamesLocator)
        companyNameText = self._get_element_text(companyNameElement)
        return companyNameText

    def get_company_full_address(self, officeDataCell):
        """
            Gets the company full address from page (address, phone, post index etc...).
        """
        fullAddressElements = self._find_sub_elements(officeDataCell, self.__fullAddressesLocator)
        fullAddressText = ""
        for element in fullAddressElements:
            fullAddressText += self._get_element_text(element) + ", "
        # Remove the trailing comma and space
        fullAddressText = fullAddressText.rstrip(", ")
        return fullAddressText

    def get_offices_data(self):
        """
            Gets the company offices data from the page (country, name, address etc...).
        """
        officesDataCellsElements = self._find_elements(self.__officesDataCellLocator)
        officesData = []
        for officeDataCell in officesDataCellsElements:
            country = self.get_country_name(officeDataCell)
            companyName = self.get_company_name(officeDataCell)
            companyFullAddress = self.get_company_full_address(officeDataCell)
            officeEntry = [country, companyName, companyFullAddress]
            officesData.append(officeEntry)
            # Check if each piece of data is valid
            if not country or not companyName or not companyFullAddress:
                raise ValueError("Error: Collected data is missing some fields")
        return officesData

