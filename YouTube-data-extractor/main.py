import sys

def main():
    print("\n==== YouTube Data Extractor ====\n")
    print("1. Description Extractor")
    print("2. Comment Extractor")
    print("3. Metadata Extractor")
    print("4. Channel Video Insights Scraper")
    print("5. Exit\n")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        from description_extractor.main import run
        run()

    elif choice == "2":
        from comment_extractor.main import run
        run()

    elif choice == "3":
        from metadata_extractor.main import run
        run()

    elif choice == "4":
        from channel_video_insights_scraper.main import run
        run()

    elif choice == "5":
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
