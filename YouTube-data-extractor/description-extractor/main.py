import requests
import re
from bs4 import BeautifulSoup

# 🔥 user input
working_link = input("Enter YouTube video URL: ")

# 🔥 header add (important)
headers = {
    "User-Agent": "Mozilla/5.0"
}

soup = BeautifulSoup(requests.get(working_link, headers=headers).content, "html.parser")

video_title = soup.text.title().split("|")[0].strip()
print("\t\n\n", video_title, "\n\n\n")

pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')

# 🔥 safe extraction (crash avoid)
matches = pattern.findall(str(soup))
description = matches[0].replace('\\n','\n') if matches else "Description not found"

print(description)

# 🔥 filename safe (basic)
safe_title = re.sub(r'[\\/*?:"<>|]', "", video_title)

with open(f"{safe_title}.txt", "w", encoding="utf-8") as f:
    f.write(description)
