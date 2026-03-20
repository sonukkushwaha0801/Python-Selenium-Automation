from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run():
    # 🔗 User input
    video_url = input("Enter YouTube video URL: ")

    # 🚀 Open Chrome
    driver = webdriver.Chrome()
    driver.get(video_url)

    time.sleep(5)

    # 📜 Scroll to load comments
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    # 💬 Extract comments
    usernames = driver.find_elements(By.XPATH, '//*[@id="author-text"]')
    comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

    print("\n--- Comments ---\n")

    comment_list = []
    for i, comment in enumerate(comments, start=1):
        text = comment.text
        print(f"{i}. {text}\n")
        comment_list.append(text)

    # 💾 Save to file
    with open("youtube_comments.txt", "w", encoding="utf-8") as f:
        for user, comment in zip(usernames, comments):
            line = f"{user.text.strip()} : {comment.text.strip()}"
            print(line)
            f.write(line + "\n")

    print("✅ Comments saved successfully!")

    driver.quit()


# 🔥 Direct run support
if __name__ == "__main__":
    run()
