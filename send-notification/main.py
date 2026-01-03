from notifypy import Notify
import time

notification = Notify()
notification.title = "Health Alert"
notification.message = "Time to drink water and stretch!"

print("Reminder script started. Press Ctrl+C to stop.")

try:
    while True:
        notification.send()
        print("Notification sent!")
        # Wait for 30 minutes
        time.sleep(1800) 
except KeyboardInterrupt:
    print("\nReminder script stopped.")