import pandas as pd
import os
from config import OUTPUT_FILE


def save_results(success_accounts, failed_accounts):
    os.makedirs(os.path.dirname(str(OUTPUT_FILE)), exist_ok=True)

    success_df = pd.DataFrame(success_accounts, columns=["Email", "Password", "Status"])

    failed_df = pd.DataFrame(failed_accounts, columns=["Email", "Password", "Reason"])

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        success_df.to_excel(writer, sheet_name="Success", index=False)
        failed_df.to_excel(writer, sheet_name="Failed", index=False)

    print(f"Results saved at: {OUTPUT_FILE}")


if __name__ == "__main__":
    success_accounts = [
        ["college001@axiscolleges.in", "college001", "Login Successful"]
    ]
    failed_accounts = [["college002@axiscolleges.in", "college002", "Login Failed"]]
    save_results(success_accounts, failed_accounts)
