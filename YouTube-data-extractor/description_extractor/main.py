import requests
import re
from bs4 import BeautifulSoup


def run():
    # 🔥 user input
    working_link = input("Enter YouTube video URL: ")

    # 🔥 header add (important)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    soup = BeautifulSoup(
        requests.get(working_link, headers=headers).content,
        "html.parser"
    )

    # 🎬 Title
    video_title = soup.text.title().split("|")[0].strip()
    print("\n\n", video_title, "\n\n")

    # 📄 Extract description
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    matches = pattern.findall(str(soup))

    description = matches[0].replace('\\n', '\n') if matches else "Description not found"

    print(description)

    # 💾 Safe filename
    safe_title = re.sub(r'[\\/*?:"<>|]', "", video_title)

    with open(f"{safe_title}.txt", "w", encoding="utf-8") as f:
        f.write(description)

    print("\n✅ Description saved successfully!")


# 🔥 Direct run support
if __name__ == "__main__":
    run()
