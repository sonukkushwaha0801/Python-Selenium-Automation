from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_page_urls(product_name):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    page_urls = []

    try:
        driver.get("https://www.amazon.in/")

        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )

        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

        pagination = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//span[contains(@class, "s-pagination-item")]')
            )
        )

        max_pages = 1
        for page in pagination:
            text = page.text.strip()
            if text.isdigit():
                max_pages = max(max_pages, int(text))

        for page in range(1, max_pages + 1):
            url = f"https://www.amazon.in/s?k={product_name}&page={page}"
            page_urls.append(url)

    finally:
        driver.quit()

    return page_urls


if __name__ == "__main__":
    product_name = "laptop"
    print(get_page_urls(product_name))
