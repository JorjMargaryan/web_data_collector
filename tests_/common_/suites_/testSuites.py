import unittest
from tests_.testCases_.functionalTests import FunctionalTests
from tests_.testCases_.acceptanceTests import AcceptanceTests


class TestSuites:
    """
        This class provides methods to create test suites for various testing scenarios, allowing for organized and
        purpose-driven test case grouping.
    """
    def get_functional_tests_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(FunctionalTests))
        return suite

    def get_acceptance_tests_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(AcceptanceTests))
        return suite

    def get_regression_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(FunctionalTests))
        suite.addTest(unittest.makeSuite(AcceptanceTests))
        return suite
