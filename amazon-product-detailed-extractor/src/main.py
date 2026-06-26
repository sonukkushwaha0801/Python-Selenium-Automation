from page_extractor import get_page_urls
from product_url_extractor import get_product_urls
from product_details_extractor import get_product_details
from exporter import save_to_excel
import time

if __name__ == "__main__":
    start = time.time()
    product_name = input("Enter the product name: ")

    print("Extracting page URLs...")
    page_urls = get_page_urls(product_name)
    print("Extracting product URLs...")
    product_urls = get_product_urls(page_urls)
    print("Extracting product details...")
    products = get_product_details(product_urls)
    print("Saving to Excel...")
    save_to_excel(products, product_name)
    print("Done!")
    end = time.time()
    print(f"Total time taken: {end - start} seconds")
