# Timedelta function demonstration
from datetime import datetime, timedelta
 
# Using current time
ini_time_for_now = datetime.now()
 
# printing initial_date
print("initial_date", str(ini_time_for_now))
 
# Some another datetime
new_final_time = ini_time_for_now + \
    timedelta(days=2)
 
# printing new final_date
print("new_final_time", str(new_final_time))
 
 
# printing calculated past_dates
print('Time difference:', str(new_final_time -
                              ini_time_for_now))