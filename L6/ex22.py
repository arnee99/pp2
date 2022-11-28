from datetime import datetime
from pytz import timezone
 
format = "%Y-%m-%d %H:%M:%S %Z%z"
 
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
 
timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']
 
for tzone in timezones:
 
    # Convert to Asia/Kolkata time zone
    now_asia = now_utc.astimezone(timezone(tzone))
    print(now_asia.strftime(format))