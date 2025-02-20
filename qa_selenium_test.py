import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.headless = False  # Set to True if you want to run in the background
    service = Service(ChromeDriverManager().install())  # Auto-install ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case: Validate search functionality for "New York"
def test_search_functionality(driver):
    # Step 1: Open the Table Search Demo page
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    time.sleep(10)  # Wait for page to load

    # Step 2: Locate the search box and enter "New York"
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys("New York")
    time.sleep(10)  # Wait for filtering to take effect

    # Step 3: Count visible rows in the table
    visible_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style, 'display: none'))]")
    row_count = len(visible_rows)

    # Take a screenshot of the filtered results
    driver.save_screenshot("search_results.png")
    print("Screenshot saved as 'search_results.png'")

    # Step 4: Validate that exactly 5 entries are shown
    assert row_count == 5, f"Test Failed: Expected 5 rows, but found {row_count}"
    print("Test Passed: Search functionality works correctly!")
