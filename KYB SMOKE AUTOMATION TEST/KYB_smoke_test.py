from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Setup
BASE_URL = "https://knowyourbodynepal.org/"
driver = webdriver.Chrome()  
driver.maximize_window()

# Helper functions
def test_page_load(url, element_selector=None, description=""):
    try:
        driver.get(url)
        time.sleep(2) 
        if element_selector:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            print(f"[PASS] {description} - Element found")
        else:
            print(f"[PASS] {description} - Page loaded successfully")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"[FAIL] {description} - {str(e)}")

# Smoke Testing....."KYB WEBSITE" BY KUSHAL NIRAULA
try:
    print("=== Starting Smoke Tests ===\n")

    # 1. Home page
    test_page_load(BASE_URL, "header", "Home Page")

    # 2. About Us
    test_page_load(BASE_URL + "about", "h1", "About Us Page")

    # 3. Programs
    test_page_load(BASE_URL + "programs", "h1", "Programs Page")

    # 4. Resources
    test_page_load(BASE_URL + "resources", "h1", "Resources Page")

    # 5. Blog
    test_page_load(BASE_URL + "blog", "h1", "Blog Page")

    # 6. Contact
    test_page_load(BASE_URL + "contact", "form", "Contact Page")



finally:
    print("\n=== Smoke Test Completed ===")
    driver.quit()
