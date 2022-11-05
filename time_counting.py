from datetime import datetime

now = datetime.now()

time = now.strftime("%Y-%m-%d")
print("time:", time)