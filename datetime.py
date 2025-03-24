import datetime

target_time = datetime.datetime(2027,1,2,12,5,30)
current_time = datetime.datetime.now()
if target_time < current_time:
    print(f"target time less than {current_time} ---")
else:
    print(f"target time not pass {target_time} ---")
