from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from sources_.navigationBar_.navigationBar import NavigationBar
from sources_.navigationBar_.resourcesArea import ResourcesArea
from sources_.pages_.contactsPage import ContactsPage
from scripts_.saveFiles import SaveFiles

from common_.utilities_.customLogger import logger


def main(outputFilePath):
    """
        Main function to automate the process of navigating to a website,
        performing actions, and saving office data to a CSV file.

        Args:
            outputFilePath (str): The path to the output CSV file.
    """
    # Options for running Firefox in headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")  # Disable sandbox mode

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        # Navigate to the website
        driver.get("https://www.onlyoffice.com")

        # Perform actions
        navBarObj = NavigationBar(driver)
        navBarObj.move_mouse_to_resources_button()
        navBarObj.wait_until_the_hovered_area_opens()

        resourcesObj = ResourcesArea(driver)
        resourcesObj.click_to_contacts_button()

        # Get office data and save to CSV
        contactsPageObj = ContactsPage(driver)
        data = contactsPageObj.get_offices_data()
        saveFileObj = SaveFiles()
        saveFileObj.save_as_csv_file(outputFilePath, data)

    except Exception as e:
        from exitCodes import MessageCodes, UNEXPECTED_BEHAVIOR
        print("An error occurred while parsing office data. Please check the website structure and your internet connection.")
        logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
        exit(UNEXPECTED_BEHAVIOR)
    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    import argparse
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Save office data to a CSV file.")
    parser.add_argument("outputFilePath", type=str, nargs='?', default="officeData.csv", help="The path to the output CSV file.")
    args = parser.parse_args()

    # Call the main function with the provided output file path
    main(args.outputFilePath)
