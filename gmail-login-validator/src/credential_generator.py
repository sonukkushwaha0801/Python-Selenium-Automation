from config import NUMBER_OF_STUDENTS


def generate_credentials():
    accounts = []

    for student_id in range(1, NUMBER_OF_STUDENTS + 1):
        username = f"test001{student_id:03d}"

        account = {"email": f"{username}@collegename.in", "password": username}

        accounts.append(account)

    return accounts


if __name__ == "__main__":
    credentials = generate_credentials()
    for i, account in enumerate(credentials):
        if i < 5:  # Print only the first 5 accounts for verification
            print(f"{i}: {account['email']} - {account['password']}")
