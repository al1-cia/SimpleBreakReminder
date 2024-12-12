import time
from plyer import notification

def remind_to_take_break():
    while True:
        # Show the notification
        notification.notify(
            title="Rest your eyes!",
            message="It's been 20 minutes. Look at something 20 feet away for 20 seconds.",
            timeout=20  # Notification duration in seconds
        )
        # Wait for 20 minutes (1200 seconds). Use a loop because longer durations reduce timing accuracy.
        for i in range(100):
           time.sleep(12)

        

if __name__ == "__main__":
    remind_to_take_break()
