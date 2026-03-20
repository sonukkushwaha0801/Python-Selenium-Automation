from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run():
    # 🔗 Input
    video_url = input("Enter YouTube video URL: ")

    # 🚀 Open Chrome
    driver = webdriver.Chrome()
    driver.get(video_url)

    time.sleep(5)

    # 🎬 Title
    title = driver.find_element(By.XPATH, '//*[@id="title"]/h1').text

    # 📺 Channel Name & Subscriber Count
    channel = driver.find_element(By.XPATH, '//*[@id="text"]/a').text
    subscriber_count = driver.find_element(By.XPATH, '//*[@id="owner-sub-count"]').text

    # 👀 Views + Date
    views = driver.find_element(By.XPATH, '//*[@id="info"]/span[1]').text
    views_date = driver.find_element(By.XPATH, '//*[@id="info"]/span[3]').text

    # 👍 Likes (safe handling)
    try:
        likes = driver.find_element(
            By.XPATH,
            '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/div[2]'
        ).text
    except:
        likes = "Not available"

    # 🖨 Output
    print("\n--- Video Metadata ---\n")
    print(f"Title             : {title}")
    print(f"Channel           : {channel}")
    print(f"Subscriber Count  : {subscriber_count}")
    print(f"Views             : {views}")
    print(f"Views/Date        : {views_date}")
    print(f"Likes             : {likes}")

    # 💾 Save to file
    with open("video_metadata.txt", "w", encoding="utf-8") as f:
        f.write(f"Title             : {title}\n")
        f.write(f"Channel           : {channel}\n")
        f.write(f"Subscriber Count  : {subscriber_count}\n")
        f.write(f"Views             : {views}\n")
        f.write(f"Views/Date        : {views_date}\n")
        f.write(f"Likes             : {likes}\n")

    print("\n✅ Metadata saved successfully!")

    driver.quit()


# 🔥 Direct run support
if __name__ == "__main__":
    run()
