import win11toast
from win11toast import ToastNotification

# Create the notification with required parameters
A = ToastNotification(app_id="Drink Water App", title="Drink Water Reminder", message="Time to drink water!")

# Show the toast
A.show()

# A = ToastNotification(app_id="Drink Water Reminder",title="Time to drink water", msg="Stay hydrated for better health")
# A.show_toast()
# toast('Hello Naveen', 'Drink water notification.')

# Display a clickable notification that opens a URL on click
# The program will run in the background to listen for the click action
# toast('Hello Naveen', 'Click to open Bottle', on_click='https://www.python.org')

# import os
# import time

# REPEAT_INTERVAL = 60 # 1 hour in seconds

# while True:
#     os.system('notify-send "Drink Water" "Time to drink water!"')
#     time.sleep(REPEAT_INTERVAL)    
