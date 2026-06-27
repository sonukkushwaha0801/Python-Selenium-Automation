from pathlib import Path

NUMBER_OF_STUDENTS = 135
LOGIN_URL = "https://accounts.google.com/"
WAIT_TIME = 10
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "data" / "gmail_login_results.xlsx"
print(f"Output file path: {OUTPUT_FILE}")
