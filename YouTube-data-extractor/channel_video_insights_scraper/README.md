# Channel Video Insights Scraper

## 🚀 Overview

A Python-based automation tool that extracts detailed video insights from a YouTube channel using Selenium.
It dynamically navigates the channel's video section and collects structured data for analysis.

## 🧠 Features

* Accepts YouTube channel URL as input
* Automatically navigates to the "Videos" section
* Extracts video title and URL
* Extracts views count
* Extracts upload time
* Extracts video duration
* Extracts channel name (uploaded by)
* Saves data in a structured format

## 🛠 Tech Stack

* Python
* Selenium

## ⚙️ How It Works

The script launches a Chrome browser, loads the YouTube channel page, switches to the videos tab, scrolls to load content, and extracts video data using dynamic DOM interaction.

## ▶️ Run the Project

```bash id="2v8t0d"
python main.py
```

## 📊 Output Format

```id="3l05bh"
Title, Link, Views, Uploaded_by, Time_duration
```

## 🎯 Purpose

Built to demonstrate real-world browser automation and large-scale data extraction from dynamic web platforms for analysis and insights.

## 👨‍💻 Author

**Sonu Kumar Kushwaha**

## 📌 Note

This project is created for educational purposes and relies on YouTube’s dynamic page structure, which may change over time.

