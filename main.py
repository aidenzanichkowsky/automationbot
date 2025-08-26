import sys
from bots import file_organizer, scraper, reminder

def menu():
    print("\n=== Automation Bot Suite ===")
    print("1. Organize Downloads Folder")
    print("2. Scrape Latest News Headlines")
    print("3. Reminder Notification")
    print("4. Exit")

while True:
    menu()
    choice = input("Select a bot (1-4): ")

    if choice == "1":
        file_organizer.run()
    elif choice == "2":
        scraper.run()
    elif choice == "3":
        reminder.run()
    elif choice == "4":
        print("Exiting... Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Try again.")
