
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TestWikipedia():
    driver = webdriver.Chrome()

    driver.get("https://en.wikipedia.org")

    search = driver.find_element(By.CLASS_NAME, "vector-search-box-input")
    search.send_keys("wake tech")
    search.send_keys(Keys.RETURN)

    header = ""
    try:
        header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        assert header.text == "Wake Technical Community College"
        driver.quit()
    except:
        driver.quit()

test_TestWikipedia()
