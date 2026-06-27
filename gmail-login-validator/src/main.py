from credential_generator import generate_credentials
from login_validator import login_account
from excel_handler import save_results


def main():
    accounts = generate_credentials()

    success_accounts = []
    failed_accounts = []

    for account in accounts:
        email = account["email"]
        password = account["password"]

        print(f"Checking: {email}")

        status, message = login_account(email, password)

        if status:
            success_accounts.append([email, password, message])
            print(f"SUCCESS: {email}")
        else:
            failed_accounts.append([email, password, message])
            print(f"FAILED: {email} -> {message}")

    save_results(success_accounts, failed_accounts)


if __name__ == "__main__":
    main()
