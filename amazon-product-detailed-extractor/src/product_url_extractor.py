from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_product_urls(page_urls):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    product_urls = set()

    try:
        for page_url in page_urls:
            driver.get(page_url)
            product_elements = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//a[contains(@class,"a-link-normal")]')
                )
            )
            for product in product_elements:
                url = product.get_attribute("href")
                if url and "/dp/" in url:
                    clean_url = url.split("?")[0]
                    product_urls.add(clean_url)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

    return list(product_urls)
