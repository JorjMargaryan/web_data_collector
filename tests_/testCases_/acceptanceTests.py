from tests_.baseTest import BaseTest

from sources_.navigationBar_.navigationBar import NavigationBar
from sources_.navigationBar_.resourcesArea import ResourcesArea
from sources_.pages_.contactsPage import ContactsPage
from scripts_.saveFiles import SaveFiles


class AcceptanceTests(BaseTest):
    def setUp(self):
        super().setUp()
        # Pre-Condition
        self.navBarObj = NavigationBar(self.driver)
        self.resourcesObj = ResourcesArea(self.driver)
        self.contactsPageObj = ContactsPage(self.driver)
        self.saveFilesObj = SaveFiles()

        self.createdFiles = []  # List to track created files

    def test_main_page_opening_functionality(self):
        """
            Test Case: Verify is the main Page opened.
            Expected Result: The page should be opened and the title should contain page name.
        """
        self.assertIn("ONLYOFFICE", self.driver.title, "Error: The page is not opened, the page title does not contain page name.")
        self.assertTrue(self.navBarObj.is_navigation_bar_visible(), "Error: The page is not opened, the navigation bar is not visible. ")

    def test_resources_area_opens_on_hover(self):
        """
            Test Case: Verify is the Resources Area Opens on Hover
            Expected Result: The resources area should open.
        """
        # Act
        self.navBarObj.move_mouse_to_resources_button()

        # Assertion
        self.assertTrue(self.navBarObj.is_area_of_hovered_element_visible(), "Error: The Resources area is not opened after hovering over Resources button. ")

    def test_contacts_page_opens_on_click(self):
        """
            Test Case: Verify is the Contacts Page Opens on Click
            Expected Result: The contacts page should open.
        """
        # Act
        self.navBarObj.move_mouse_to_resources_button()
        self.navBarObj.wait_until_the_hovered_area_opens()
        self.resourcesObj.click_to_contacts_button()

        # Assertion
        self.assertTrue(self.contactsPageObj.is_contacts_page_opened(), "Error: The Contacts page is not opened, but should be.")

    def test_data_collection_from_page(self):
        """
            Test Case: Verify Data Collection from Page
            Expected Result: The office data should be collected and be in the expected format
        """
        # Act
        self.navBarObj.move_mouse_to_resources_button()
        self.navBarObj.wait_until_the_hovered_area_opens()
        self.resourcesObj.click_to_contacts_button()
        data = self.contactsPageObj.get_offices_data()

        # Assertion
        self.assertIsNot(data, None, "Error: Data is None")
        self.assertIsInstance(data, list, "Error: Data is not an instance of List")
        self.assertGreater(len(data), 0, "Error: Offices data list is empty")

    def test_save_csv_file(self):
        """
            Test Case: Verify Save CSV File
            Expected Result: The CSV file should be created and contain the data.
        """
        # Act
        sampleData = [
            ["USA", "OnlyOffice Inc.", "1234 Elm Street, Anytown, USA"],
            ["Germany", "OnlyOffice GmbH", "5678 Oak Street, Berlin, Germany"]
        ]
        outputFile = "officeData.csv"
        self.saveFilesObj.save_as_csv_file(outputFile, sampleData)

        # Assertion
        with open(outputFile, 'r') as file:
            content = file.read()
        self.assertGreater(len(content), 0, "Error: CSV file is empty, but should not be.")
        self.createdFiles.append(outputFile)

    def tearDown(self):
        import os
        from common_.utilities_.customLogger import logger
        for filePath in self.createdFiles:
            if os.path.exists(filePath):
                os.remove(filePath)
                logger("INFO", f"The file '{filePath}' is removed successfully")
        super().tearDown()
