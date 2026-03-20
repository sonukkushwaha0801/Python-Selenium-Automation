from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re


def convert_to_int(value: str) -> int:
    value = value.strip().upper()

    if value.endswith('K'):
        return int(float(value[:-1]) * 1_000)
    elif value.endswith('M'):
        return int(float(value[:-1]) * 1_000_000)
    else:
        return int(value.replace(',', ''))


def run():
    # 🔹 User input
    channel_url = input("Enter YouTube Channel URL: ").strip()

    driver = webdriver.Chrome()
    driver.get(channel_url + "/videos")
    driver.maximize_window()

    body = driver.find_element(By.CSS_SELECTOR, "body")

    # 🔹 Get total videos
    no_of_video = driver.find_element(
        By.XPATH,
        '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[3]/span'
    ).text

    no_of_video = convert_to_int(no_of_video.split()[0])

    # 🔹 Scroll calculation
    scrolls = round(no_of_video / 28)

    for _ in range(scrolls):
        body.send_keys(Keys.END)
        time.sleep(2)

    html = driver.page_source
    channel_name = driver.title.replace(" - YouTube", "").strip()

    driver.quit()

    # 🔹 Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    videos = soup.find_all('div', {'id': 'dismissible'})

    # 🔹 File name dynamic
    file_name = f"{channel_name}.csv"

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Title", "Link", "Views", "Uploaded", "Duration"])

        for video in videos:
            try:
                title = video.find('yt-formatted-string', {'id': 'video-title'}).text
                link = 'https://www.youtube.com' + video.find('a', {'id': 'video-title-link'})['href']

                meta = video.find('div', {'id': 'metadata-line'}).find_all('span')
                views = meta[0].text
                uploaded = meta[1].text

                duration = video.find('span', {'id': 'text'}).text.strip()

                writer.writerow([title, link, views, uploaded, duration])

            except Exception as e:
                continue

    print(f"✅ Data saved in {file_name}")


# 🔥 Direct run support
if __name__ == "__main__":
    run()
