from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the NavigationBar class.
        """
        super().__init__(driver)

        self.__navigationBarLocator = (By.CLASS_NAME, "pushy")
        self.__resourcesButtonLocator = (By.ID, "navitem_about")
        self.__hoveredAreaLocator = (By.ID, "navitem_about_menu")

    def is_navigation_bar_visible(self):
        """
           Checks whether the navigation bar is visible.
        """
        return self._is_element_visible(self.__navigationBarLocator)

    def wait_until_the_hovered_area_opens(self):
        """
            Waits until the area corresponding to the hovered element is opened.
        """
        if not self.is_area_of_hovered_element_visible():
            raise Exception("The corresponding area is not opened after hovering over the element.")

    def move_mouse_to_resources_button(self):
        """
            Moves the mouse pointer over the Resources button in the navigation bar, simulating a hover action.
        """
        resourcesButtonElement = self._find_element(self.__resourcesButtonLocator)
        self._mouse_move_to_element(resourcesButtonElement)

    def is_area_of_hovered_element_visible(self):
        """
           Checks if the element's property 'Display' is 'block' which means the area corresponding to the hovered element is opened.
        """
        hoveredAreaElement = self._find_element(self.__hoveredAreaLocator)
        afterHoverDisplayValue = hoveredAreaElement.value_of_css_property("display")
        if afterHoverDisplayValue == "block":
            return True
        else:
            return False
