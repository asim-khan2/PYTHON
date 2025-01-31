import time
# t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
# print(hour)
# print(t)

if (hour>=7 and hour <= 12):
    print("Good morning Asim Khan")
elif (hour>=12 and hour <= 17):
    print("Good Afternoon Asim Khan")
else :
    print("Good night Asim Khan")

