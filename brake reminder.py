from plyer import notification
import time
import screen_brightness_control as sbc
import os
computer_name = os.environ.get("COMPUTERNAME")

def remind_to_take_break():
    while True:
        sbc.set_brightness(0)
        notification.notify(
            title="TAKE A BREAK",
            message=f"HEY {computer_name}! AN HOUR PASSED!⌚ IT'S TIME TO TAKE A BREAK.",
            app_name="Break Reminder App",  # Corrected app name
            timeout=10  # Notification stays for 10 seconds
        )
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    remind_to_take_break()