# YouTube Comment Extractor

## 🚀 Overview

A Python-based tool that extracts comments from a YouTube video using Selenium automation.
It scrolls through the page, collects usernames and comments, and saves them in a structured format.

## 🧠 Features

* Accepts YouTube video URL as input
* Automatically scrolls to load comments
* Extracts usernames and their comments
* Saves data in `username : comment` format
* Outputs data to a text file

## 🛠 Tech Stack

* Python
* Selenium

## ⚙️ How It Works

The script opens the YouTube video in a Chrome browser, scrolls to load comments dynamically, and extracts user-comment pairs using XPath selectors.

## ▶️ Run the Project

```bash
python main.py
```

## 🎯 Purpose

Built to demonstrate browser automation and dynamic data extraction from JavaScript-rendered web pages.

## 👨‍💻 Author

**Sonu Kumar Kushwaha**

## 📌 Note

This project is created for educational purposes and relies on YouTube’s page structure, which may change over time.

