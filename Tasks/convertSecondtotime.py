from datetime import datetime,time,date

second = 21328971

print(datetime.fromtimestamp(
    int(second)
).strftime("%Y,%B,%d")
)