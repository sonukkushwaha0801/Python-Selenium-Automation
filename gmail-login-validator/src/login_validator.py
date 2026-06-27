from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import LOGIN_URL, WAIT_TIME
import time


def login_account(email, password):
    driver = webdriver.Chrome()

    try:
        driver.fullscreen_window()
        driver.get(LOGIN_URL)

        current_page = driver.current_url

        # Email Input
        email_box = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_box.send_keys(email + Keys.ENTER)

        # Password Input
        password_box = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
            )
        )
        password_box.send_keys(password + Keys.ENTER)

        time.sleep(5)

        # Wait for login result
        try:
            WebDriverWait(driver, 20).until(
                lambda d: "mail.google.com" in d.current_url
            )

            driver.find_element(By.XPATH, '//a[contains(@href,"SignOutOptions")]')
            return True, "Login Successful"

        except Exception as e:
            return False, f"Login Failed: {str(e)}"

    finally:
        driver.quit()


if __name__ == "__main__":
    email = "2026MBA001@Collegesname.in"
    password = "2026MBA001"

    status, message = login_account(email, password)
    print(status, message)
