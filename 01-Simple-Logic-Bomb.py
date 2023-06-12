from datetime import date

today = date.today()
target_date = date(today.year, 12, 25)

def not_bad_message():
    print(">> MERRY CHRISTMAS <<")
    print(" ")
    exit()

def trigger_not():
    if (today == target_date):
        not_bad_message()

print("Running the Program... ")
trigger_not()
print("Everything is running correctly... for now...")