working_hrs = []
weekly_hrs = 0

working_days = int(input("No of working days: "))

for i in range(0,working_days):
    daily_hrs = float(input("Working hours on day "+ str(int(i+1)) +" : "))
    working_hrs.append(daily_hrs)

for i in range(0,working_days):
    weekly_hrs = weekly_hrs + working_hrs[i]

avg_working_hrs = weekly_hrs / working_days

print("Average  working time(in Hrs) :", avg_working_hrs)