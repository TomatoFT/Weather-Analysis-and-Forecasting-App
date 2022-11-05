from datetime import datetime
from datetime import timedelta
time_step = []

for i in range(0,300):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d")
    time = datetime.strptime(time, "%Y-%m-%d")
    time = time - timedelta(days=i)
    time_step.append(time)

