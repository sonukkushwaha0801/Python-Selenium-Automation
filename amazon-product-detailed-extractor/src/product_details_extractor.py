from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_product_details(product_urls):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    all_products = []

    try:
        for url in product_urls:
            driver.get(url)

            product_data = {
                "name": "",
                "discounted_price": "",
                "mrp": "",
                "policy": "",
                "specifications": "",
                "about_item": "",
            }

            # Product Name
            try:
                product_data["name"] = wait.until(
                    EC.presence_of_element_located((By.ID, "productTitle"))
                ).text.strip()
            except:
                pass

            # Discounted Price
            try:
                product_data["discounted_price"] = driver.find_element(
                    By.CSS_SELECTOR,
                    "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative.apex-core-price-identifier > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay.apex-pricetopay-value > span:nth-child(2)",
                ).text
            except:
                pass

            # MRP
            try:
                product_data["mrp"] = driver.find_element(
                    By.XPATH, '//span[contains(@class,"a-price a-text-price")]'
                ).text
            except:
                pass

            # Policy
            try:
                bullets = driver.find_elements(
                    By.XPATH, '//*[@id="icon-farm-container"]/div/div/div[2]'
                )
                about = [
                    bullet.text.strip() for bullet in bullets if bullet.text.strip()
                ]
                product_data["policy"] = " | ".join(about)
                product_data["policy"] = product_data["policy"].replace("\n", " | ")
            except:
                pass

            # Specifications
            try:
                specs = driver.find_elements(
                    By.CSS_SELECTOR, "#productOverview_feature_div tr"
                )

                spec_list = []

                for row in specs:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    if len(cols) >= 2:
                        key = cols[0].text.strip()
                        value = cols[1].text.strip()
                        spec_list.append(f"{key}: {value}")

                product_data["specifications"] = " | ".join(spec_list)

            except:
                pass

            # About Item
            try:
                bullets = driver.find_elements(
                    By.CSS_SELECTOR, "#feature-bullets ul li span"
                )
                about = []
                for bullet in bullets:
                    text = bullet.text.strip()
                    if text:
                        about.append(text)
                product_data["about_item"] = " | ".join(about)
            except:
                pass

            all_products.append(product_data)

    finally:
        driver.quit()

    return all_products
