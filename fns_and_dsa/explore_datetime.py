from datetime import datetime
from datetime import timedelta

def display_current_datetime():

  date_now = datetime.now()

  return date_now

def calculate_future_date(days_to_be_added, current_date):
  days_to_be_added_date = timedelta(days = days_to_be_added)
  end_date = current_date + days_to_be_added_date

  return end_date

current_date = display_current_datetime()

print('Current date and time: ' + current_date.strftime("%Y-%m-%d %H:%M:%S"))

days = int(input("Enter the number of days to add to the current date: "))


future_date = calculate_future_date(days, current_date)

print(f'Future date: ' + future_date.strftime('%Y-%m-%d'))