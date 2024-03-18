import pytest
from Base.webDriverFactory import webDriverFactory
import utilities.customLogger as cs
import logging

log = cs.customLogger()

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    log.info("Running one time setUp")
    wdf = webDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.info("Running one time teardown")
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")