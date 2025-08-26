import time
from plyer import notification

def run():
    reminder = input("Enter reminder message: ")
    minutes = int(input("Remind me in how many minutes? "))

    print(f"Reminder set! I’ll notify you in {minutes} minutes...")
    time.sleep(minutes * 60)

    notification.notify(
        title="⏰ Reminder Bot",
        message=reminder,
        timeout=10
    )
