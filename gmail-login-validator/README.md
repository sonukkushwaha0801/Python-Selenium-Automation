# Gmail Login Validator

![Gmail_Banner](/assests/Banner.webp)

## Overview

Gmail Login Validator is a Python Selenium automation project designed to validate bulk Gmail credentials by automating the Google login workflow.

The system automatically:

* Generates credentials
* Attempts Gmail login
* Detects login success/failure
* Stores results into structured Excel reports

This project demonstrates practical browser automation, credential validation, workflow automation, and reporting.

---

## Features

* Bulk credential generation
* Automated Gmail login validation
* Success / Failure classification
* Excel report generation
* Exception handling
* Modular project structure

---

## Tech Stack

* Python
* Selenium
* Pandas
* OpenPyXL

---

## Project Structure

```bash
gmail-login-validator/
│
├── assets/
│   └── banner.png
│
├── data/
│   └── gmail_login_results.xlsx   # Generated after script execution
│
├── src/
│   ├── config.py
│   ├── credential_generator.py
│   ├── login_validator.py
│   ├── excel_handler.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Workflow

```text
Generate Credentials
       ↓
Validate Gmail Login
       ↓
Classify Result
       ↓
Success / Failed
       ↓
Generate Excel Report
```

---

## Installation

Clone repository:

```bash
git clone <your-repository-url>
cd gmail-login-validator
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Linux / Mac

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python src/main.py
```

---

## Output

After execution, an Excel report is generated:

```bash
data/gmail_login_results.xlsx
```

The report contains 2 sheets:

### Success Sheet

| Email                                         | Password | Status           |
| --------------------------------------------- | -------- | ---------------- |
| [test001@gmail.com](mailto:test001@gmail.com) | test001  | Login Successful |
| [test002@gmail.com](mailto:test002@gmail.com) | test002  | Login Successful |

---

### Failed Sheet

| Email                                         | Password | Reason              |
| --------------------------------------------- | -------- | ------------------- |
| [test003@gmail.com](mailto:test003@gmail.com) | test003  | Invalid Credentials |
| [test004@gmail.com](mailto:test004@gmail.com) | test004  | Recovery Required   |

---

## Use Cases

* Bulk credential validation
* Automation testing
* Browser automation learning
* QA workflow automation

---

## Future Improvements

* Better failure classification
* CAPTCHA handling
* Retry mechanism
* Logging support
* Single browser session optimization

---

## Author

**Author:** Sonu Kumar Kushwaha [sonukkushwaha0801]
**Collaborator:** Zenithra [zenithrahub]
