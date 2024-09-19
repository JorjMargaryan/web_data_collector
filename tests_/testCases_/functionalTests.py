from tests_.baseTest import BaseTest

from sources_.navigationBar_.navigationBar import NavigationBar
from sources_.navigationBar_.resourcesArea import ResourcesArea
from sources_.pages_.contactsPage import ContactsPage
from scripts_.saveFiles import SaveFiles


class FunctionalTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.createdFiles = []  # List to track created files

    def test_data_collection_and_file_saving_functionality(self):
        """
            Test Case: Verify the functionality of data collection from the contacts page and saving it to a CSV file.
        """
        # Pre-Condition
        navBarObj = NavigationBar(self.driver)
        self.assertTrue(navBarObj.is_navigation_bar_visible(), "Error: The page is not opened, the navigation bar is not visible. ")
        navBarObj.move_mouse_to_resources_button()
        navBarObj.wait_until_the_hovered_area_opens()
        self.assertTrue(navBarObj.is_area_of_hovered_element_visible(), "Error: The Resources area is not opened after hovering over Resources button. ")

        resourcesObj = ResourcesArea(self.driver)
        resourcesObj.click_to_contacts_button()

        contactsPageObj = ContactsPage(self.driver)
        self.assertTrue(contactsPageObj.is_contacts_page_opened(), "Error: The Contacts page is not opened, but should be.")

        # Act
        data = contactsPageObj.get_offices_data()
        self.assertGreater(len(data), 0, "Error: Offices data list is empty")
        outputFilePath = "data.csv"
        saveFilesObj = SaveFiles()
        saveFilesObj.save_as_csv_file(outputFilePath, data)

        # Assertion
        with open(outputFilePath, 'r') as file:
            content = file.read()
        self.assertGreater(len(content), 0, "Error: CSV file is empty, but should not be.")
        self.createdFiles.append(outputFilePath)

    def tearDown(self):
        import os
        from common_.utilities_.customLogger import logger
        for filePath in self.createdFiles:
            if os.path.exists(filePath):
                os.remove(filePath)
                logger("INFO", f"The file '{filePath}' is removed successfully")
        super().tearDown()
